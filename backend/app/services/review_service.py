# backend/app/services/review_service.py
from typing import Dict, Any, List
from datetime import datetime
from sqlalchemy.orm import Session
from app.services.ai_service import AIService
from app.services.github_service import GitHubService
from app.models.review import CodeReview, ReviewComment
from app.models.repository import Repository
import asyncio

class ReviewService:
    def __init__(self):
        self.ai_service = AIService()
        self.github_service = GitHubService()
    
    async def process_pull_request(self, webhook_data: Dict[str, Any], db: Session) -> bool:
        """Process a pull request for review"""
        try:
            pr_data = webhook_data["pull_request"]
            repo_data = webhook_data["repository"]
            
            # Get repository from database
            repository = db.query(Repository).filter(
                Repository.github_id == str(repo_data["id"])
            ).first()
            
            if not repository or not repository.auto_review_enabled:
                return False
            
            # Create review record
            review = CodeReview(
                repository_id=repository.id,
                pull_request_id=str(pr_data["number"]),
                commit_sha=pr_data["head"]["sha"],
                status="pending"
            )
            db.add(review)
            db.commit()
            
            # Process files asynchronously
            await self._analyze_pr_files(review, repo_data["full_name"], 
                                       pr_data["number"], pr_data["head"]["sha"], db)
            
            return True
            
        except Exception as e:
            print(f"Error processing PR: {e}")
            return False
    
    async def _analyze_pr_files(self, review: CodeReview, repo_full_name: str, 
                               pr_number: int, commit_sha: str, db: Session):
        """Analyze files in a pull request"""
        try:
            # Get access token (implement OAuth flow)
            access_token = "github_access_token"  # TODO: Implement proper token management
            
            # Get changed files
            files = await self.github_service.get_pull_request_files(
                repo_full_name, pr_number, access_token
            )
            
            all_issues = []
            total_quality_score = 0
            files_analyzed = 0
            
            for file_data in files:
                if file_data.get("status") == "removed":
                    continue
                
                file_path = file_data["filename"]
                file_extension = file_path.split(".")[-1] if "." in file_path else ""
                
                # Skip non-code files
                if file_extension not in ["py", "js", "ts", "java", "go", "cpp", "c", "rb", "php"]:
                    continue
                
                # Get file content
                content = await self.github_service.get_file_content(
                    repo_full_name, file_path, commit_sha, access_token
                )
                
                if not content:
                    continue
                
                # Analyze with AI
                language = self._get_language_from_extension(file_extension)
                
                # Run parallel analysis
                quality_result, security_issues, performance_issues = await asyncio.gather(
                    self.ai_service.analyze_code_quality(content, language, file_path),
                    self.ai_service.detect_security_vulnerabilities(content, language),
                    self.ai_service.suggest_performance_improvements(content, language)
                )
                
                # Process results
                if "quality_score" in quality_result:
                    total_quality_score += quality_result["quality_score"]
                    files_analyzed += 1

                # Store issues
                all_issues.extend(security_issues)
                all_issues.extend(performance_issues)
                
                # Update review status
                review.status = "completed"
                review.analyzed_at = datetime.now()
                review.quality_score = total_quality_score // files_analyzed if files_analyzed > 0 else 0
                db.commit()

        except Exception as e:
            print(f"Error analyzing PR files: {e}")
            raise e
        
    def _get_language_from_extension(self, extension: str) -> str:
        """Get language from file extension"""
        extension = extension.lower()
        if extension in ["py", "pyw", "pyc", "pyo", "pyd", "pywz", "pyz"]:
            return "python"
        elif extension in ["js", "jsx", "ts", "tsx"]:
            return "javascript"
        elif extension in ["java"]:
            return "java"
        elif extension in ["go"]:
            return "go"
        elif extension in ["cpp", "c", "h", "hpp"]:
            return "c++"
        elif extension in ["rb"]:
            return "ruby"
        elif extension in ["php"]:
            return "php"
        return "unknown"
    
