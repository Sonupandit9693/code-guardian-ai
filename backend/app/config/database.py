# backend/app/config/database.py
import databases
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config.settings import settings
import os

# Database setup - handle both SQLite (local dev) and PostgreSQL (production)
connect_args = {}
if "sqlite" in settings.DATABASE_URL:
    connect_args = {"check_same_thread": False}
elif "postgresql" in settings.DATABASE_URL:
    connect_args = {"pool_pre_ping": True, "pool_recycle": 300}

engine = sqlalchemy.create_engine(
    settings.DATABASE_URL,
    connect_args=connect_args
)

# Use databases library for async support with PostgreSQL
if "sqlite" not in settings.DATABASE_URL:
    database = databases.Database(settings.DATABASE_URL)
else:
    database = None

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# MongoDB setup - with error handling for local development
try:
    from pymongo import MongoClient
    mongo_client = MongoClient(settings.MONGODB_URL, serverSelectionTimeoutMS=1000)
    # Test connection
    mongo_client.server_info()
    mongo_db = mongo_client.ai_code_review
except Exception:
    print("Warning: MongoDB not available, using in-memory storage for development")
    mongo_client = None
    mongo_db = None

# Redis setup - with error handling for local development
try:
    import redis
    redis_client = redis.from_url(settings.REDIS_URL, decode_responses=True, socket_connect_timeout=1)
    # Test connection
    redis_client.ping()
except Exception:
    print("Warning: Redis not available, caching disabled for development")
    redis_client = None

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
