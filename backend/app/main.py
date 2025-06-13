
# backend/app/main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import uvicorn
from app.config.settings import settings
from app.config.database import database
from app.api.v1 import auth, reviews, analytics, github
from app.api import webhooks

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    if database:  # Only connect if using async database (PostgreSQL)
        await database.connect()
    yield
    # Shutdown
    if database:  # Only disconnect if using async database
        await database.disconnect()

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0",
    description="AI-powered code review assistant",
    lifespan=lifespan
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix=f"{settings.API_V1_STR}/auth", tags=["auth"])
app.include_router(webhooks.router, prefix=f"{settings.API_V1_STR}/webhooks", tags=["webhooks"])
app.include_router(reviews.router, prefix=f"{settings.API_V1_STR}/reviews", tags=["reviews"])
app.include_router(analytics.router, prefix=f"{settings.API_V1_STR}/analytics", tags=["analytics"])
app.include_router(github.router, prefix=f"{settings.API_V1_STR}/github", tags=["github"])

@app.get("/")
async def root():
    return {"message": "AI Code Review Assistant API", "version": "1.0.0"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "database": "connected"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)