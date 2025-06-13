# AI Code Review Assistant - Development Setup

## 🚀 Quick Start

This guide will help you set up the AI Code Review Assistant for local development.

### Prerequisites

- **Python 3.11+** (we tested with Python 3.12)
- **Node.js 18+** 
- **Git**

### 🛠️ One-Command Setup

Run the automated setup script:

```bash
./scripts/dev-setup.sh
```

This will:
- Create a Python virtual environment
- Install all backend dependencies
- Install all frontend dependencies
- Set up the development environment

### 🏃 Running the Application

#### Option 1: Using Scripts (Recommended)

**Start Backend:**
```bash
./scripts/start-backend.sh
```

**Start Frontend (in a new terminal):**
```bash
./scripts/start-frontend.sh
```

#### Option 2: Manual Commands

**Backend:**
```bash
cd backend
source venv/bin/activate
export DATABASE_URL="sqlite:///./dev.db"
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Frontend:**
```bash
cd frontend
export NEXT_PUBLIC_API_URL="http://localhost:8000"
npm run dev
```

### 🌍 Access Points

- **Frontend:** http://localhost:3000
- **Backend API:** http://localhost:8000
- **API Documentation:** http://localhost:8000/docs
- **Alternative API Docs:** http://localhost:8000/redoc

### 📝 API Endpoints

The backend provides the following main endpoints:

- **Authentication:** `/api/v1/auth/*`
- **Code Reviews:** `/api/v1/reviews/*`
- **Analytics:** `/api/v1/analytics/*`
- **GitHub Integration:** `/api/v1/github/*`
- **Webhooks:** `/api/v1/webhooks/*`

### 📦 Technology Stack

#### Backend
- **FastAPI** - Modern Python web framework
- **SQLAlchemy** - Database ORM
- **SQLite** - Database (for local development)
- **Pydantic** - Data validation
- **Uvicorn** - ASGI server

#### Frontend
- **Next.js 15** - React framework
- **TailwindCSS** - Styling
- **TypeScript** - Type safety

### 🐛 Troubleshooting

#### Backend Issues

1. **Import Errors:** Make sure the virtual environment is activated
   ```bash
   cd backend && source venv/bin/activate
   ```

2. **Database Issues:** The app uses SQLite for local development, no external database required

3. **Port Conflicts:** If port 8000 is in use, modify the port in the start script

#### Frontend Issues

1. **Node Modules:** If you get module errors, reinstall dependencies
   ```bash
   cd frontend && rm -rf node_modules && npm install
   ```

2. **Build Errors:** Clear the Next.js cache
   ```bash
   cd frontend && rm -rf .next && npm run dev
   ```

### 🐳 Docker Setup (Optional)

If you prefer Docker and have connectivity to Docker Hub:

```bash
docker-compose up --build
```

**Note:** The Docker setup includes PostgreSQL, MongoDB, and Redis services, but local development works fine with just SQLite.

### 🔧 Environment Variables

For local development, the following environment variables are set automatically by the scripts:

#### Backend
- `DATABASE_URL=sqlite:///./dev.db`
- `SECRET_KEY=dev-secret-key-change-in-production`
- `DEBUG=true`

#### Frontend
- `NEXT_PUBLIC_API_URL=http://localhost:8000`
- `NODE_ENV=development`

### 🚑 Production Environment Variables

For production, you'll need to set these in your `.env` file:

```env
# Backend
DATABASE_URL=postgresql://user:password@localhost:5432/codereviewer
MONGODB_URL=mongodb://localhost:27017/codereviewer
SECRET_KEY=your-super-secret-key-here
GITHUB_CLIENT_ID=your-github-app-client-id
GITHUB_CLIENT_SECRET=your-github-app-client-secret
GITHUB_WEBHOOK_SECRET=your-webhook-secret
OPENAI_API_KEY=your-openai-api-key
SONARQUBE_TOKEN=your-sonarqube-token
REDIS_URL=redis://localhost:6379

# Frontend
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_GITHUB_CLIENT_ID=your-github-app-client-id
```

### 🎉 What's Working

✅ **Backend API Server** - FastAPI with all routes configured  
✅ **Frontend Next.js App** - React application with TailwindCSS  
✅ **API Documentation** - Automatic OpenAPI docs at `/docs`  
✅ **Development Hot Reload** - Both frontend and backend auto-reload on changes  
✅ **CORS Configuration** - Frontend can communicate with backend  
✅ **Environment Setup** - SQLite for easy local development  
✅ **Error Handling** - Graceful fallbacks for missing external services  

### 📈 Next Steps

The foundation is now ready! Next development priorities:

1. **GitHub OAuth Integration** - Connect with GitHub for authentication
2. **AI Service Integration** - Connect with OpenAI API for code analysis
3. **Database Models** - Create proper data models for reviews, users, etc.
4. **UI Components** - Build out the dashboard and review interfaces
5. **Webhook Processing** - Implement actual GitHub webhook handling
6. **Testing** - Add unit and integration tests

### 🔍 Testing the Setup

After starting both servers, test the integration:

1. Open http://localhost:3000 (should show the AI Code Review Assistant homepage)
2. Open http://localhost:8000/docs (should show the API documentation)
3. Try the `/health` endpoint in the API docs
4. Check that both servers auto-reload when you make changes

---

**🎆 Setup Complete!** You now have a fully functional development environment for the AI Code Review Assistant.

