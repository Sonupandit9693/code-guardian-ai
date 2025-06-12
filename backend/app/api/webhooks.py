# backend/app/api/webhooks.py
from fastapi import APIRouter, Request, HTTPException, Depends, BackgroundTasks
from fastapi.security import HTTPBearer
import hmac
import hashlib
import json
from app.services.github_service import GitHubService
from app.services.ai_service import AIService
from app.config.settings import settings

router = APIRouter()
security = HTTPBearer()
github_service = GitHubService()
ai_service = AIService()

def verify_github_signature(payload: bytes, signature: str) -> bool:
    """Verify GitHub webhook signature"""
    if not settings.GITHUB_WEBHOOK_SECRET:
        return True  # Skip verification in development
    
    expected_signature = hmac.new(
        settings.GITHUB_WEBHOOK_SECRET.encode(),
        payload,
        hashlib.sha256
    ).hexdigest()
    
    return hmac.compare_digest(f"sha256={expected_signature}", signature)

@router.post("/github")
async def github_webhook(request: Request, background_tasks: BackgroundTasks):
    """Handle GitHub webhook events"""
    payload = await request.body()
    signature = request.headers.get("X-Hub-Signature-256", "")
    
    if not verify_github_signature(payload, signature):
        raise HTTPException(status_code=403, detail="Invalid signature")
    
    event_type = request.headers.get("X-GitHub-Event")
    data = json.loads(payload)
    
    if event_type == "pull_request":
        if data["action"] in ["opened", "synchronize"]:
            background_tasks.add_task(process_pull_request, data)
    
    return {"status": "received"}

async def process_pull_request(data: Dict):
    """Process pull request for code review"""
    pr_data = data["pull_request"]
    repo_data = data["repository"]
    installation_id = data["installation"]["id"]
    
    # Get PR files
    files = await github_service.get_pr_files(
        repo_data["owner"]["login"],
        repo_data["name"],
        pr_data["number"],
        installation_id
    )
    
    review_comments = []
    
    for file in files:
        if file.filename.endswith(('.py', '.js', '.ts', '.java', '.cpp', '.c')):
            # Get file content
            content = await github_service.get_file_content(
                repo_data["owner"]["login"],
                repo_data["name"],
                file.filename,
                pr_data["head"]["sha"],
                installation_id
            )
            
            # Analyze with AI
            language = detect_language(file.filename)
            analysis = await ai_service.analyze_code_quality(
                content.decoded.decode(),
                file.filename,
                language
            )
            
            # Create review comments
            for suggestion in analysis.get("suggestions", []):
                review_comments.append({
                    "path": file.filename,
                    "line": suggestion.get("line", 1),
                    "body": suggestion.get("message", "")
                })
    
    # Create GitHub review
    if review_comments:
        await github_service.create_pr_review(
            repo_data["owner"]["login"],
            repo_data["name"],
            pr_data["number"],
            pr_data["head"]["sha"],
            "COMMENT",
            "🤖 AI Code Review completed",
            review_comments,
            installation_id
        )

def detect_language(filename: str) -> str:
    """Detect programming language from filename"""
    extensions = {
        '.py': 'python',
        '.js': 'javascript',
        '.ts': 'typescript',
        '.java': 'java',
        '.cpp': 'cpp',
        '.c': 'c'
    }
    
    for ext, lang in extensions.items():
        if filename.endswith(ext):
            return lang
    
    return 'unknown'