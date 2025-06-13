# backend/app/api/webhooks.py
from fastapi import APIRouter, Request, HTTPException, Depends, BackgroundTasks
from fastapi.security import HTTPBearer
import hmac
import hashlib
import json
from typing import Dict, Any
from app.config.settings import settings

router = APIRouter()
security = HTTPBearer()

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
async def github_webhook(request: Request):
    """Handle GitHub webhook events"""
    try:
        payload = await request.body()
        signature = request.headers.get("X-Hub-Signature-256", "")
        event_type = request.headers.get("X-GitHub-Event")
        
        # Basic signature verification
        if signature and not verify_github_signature(payload, signature):
            raise HTTPException(status_code=403, detail="Invalid signature")
        
        data = json.loads(payload)
        
        # Handle different webhook events
        if event_type == "pull_request":
            action = data.get("action")
            pr_number = data["pull_request"]["number"]
            repo_name = data["repository"]["full_name"]
            
            return {
                "status": "received",
                "event": event_type,
                "action": action,
                "pr_number": pr_number,
                "repository": repo_name,
                "message": "GitHub webhook received successfully"
            }
        
        return {
            "status": "received",
            "event": event_type,
            "message": f"Webhook event '{event_type}' received"
        }
        
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON payload")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Webhook processing error: {str(e)}")

@router.get("/status")
async def webhook_status():
    """Get webhook service status"""
    return {
        "status": "active",
        "webhook_secret_configured": bool(settings.GITHUB_WEBHOOK_SECRET),
        "github_client_configured": bool(settings.GITHUB_CLIENT_ID),
        "message": "Webhook service is operational"
    }
