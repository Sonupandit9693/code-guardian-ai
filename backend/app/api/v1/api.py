# backend/app/api/v1/api.py
from fastapi import APIRouter
from app.api.v1 import auth, reviews, analytics, github

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(reviews.router, prefix="/reviews", tags=["reviews"])
api_router.include_router(analytics.router, prefix="/analytics", tags=["analytics"])
api_router.include_router(github.router, prefix="/github", tags=["github"])

