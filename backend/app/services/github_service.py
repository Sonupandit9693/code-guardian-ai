# backend/app/services/github_service.py - Complete:
# - webhook_handler()
# - pull_request_analyzer()
# - comment_poster()
# - status_updater()


import github3
import httpx
from typing import Dict, List, Optional
from app.config.settings import settings
from app.utils.github_utils import create_jwt_token, get_installation_access_token

class GitHubService:
    def __init__(self):
        self.app_id = settings.GITHUB_APP_ID
        self.private_key = settings.GITHUB_PRIVATE_KEY
        self.webhook_secret = settings.GITHUB_WEBHOOK_SECRET
        
    async def get_authenticated_client(self, installation_id: int) -> github3.GitHub:
        """Get authenticated GitHub client for installation"""
        access_token = await get_installation_access_token(installation_id)
        return github3.login(token=access_token)
    
    async def get_pull_request(self, owner: str, repo: str, pr_number: int, installation_id: int):
        """Get pull request details"""
        gh = await self.get_authenticated_client(installation_id)
        repository = gh.repository(owner, repo)
        return repository.pull_request(pr_number)
    
    async def get_pr_files(self, owner: str, repo: str, pr_number: int, installation_id: int):
        """Get files changed in pull request"""
        gh = await self.get_authenticated_client(installation_id)
        repository = gh.repository(owner, repo)
        pr = repository.pull_request(pr_number)
        return list(pr.files())
    
    async def create_review_comment(self, owner: str, repo: str, pr_number: int, 
                                  commit_sha: str, path: str, line: int, 
                                  body: str, installation_id: int):
        """Create a review comment on pull request"""
        gh = await self.get_authenticated_client(installation_id)
        repository = gh.repository(owner, repo)
        pr = repository.pull_request(pr_number)
        
        return pr.create_review_comment(
            body=body,
            commit_sha=commit_sha,
            path=path,
            line=line
        )
    
    async def create_pr_review(self, owner: str, repo: str, pr_number: int,
                             commit_sha: str, event: str, body: str,
                             comments: List[Dict], installation_id: int):
        """Create a pull request review"""
        gh = await self.get_authenticated_client(installation_id)
        repository = gh.repository(owner, repo)
        pr = repository.pull_request(pr_number)
        
        return pr.create_review(
            body=body,
            event=event,  # APPROVE, REQUEST_CHANGES, COMMENT
            commit_sha=commit_sha,
            comments=comments
        )
    
    async def get_file_content(self, owner: str, repo: str, path: str, 
                             ref: str, installation_id: int):
        """Get file content from repository"""
        gh = await self.get_authenticated_client(installation_id)
        repository = gh.repository(owner, repo)
        return repository.file_contents(path, ref=ref)