# AI Code Review Assistant

An intelligent code review system that provides automated analysis, security checks, and performance optimization suggestions using AI.

## Features

- Automated code quality analysis
- Security vulnerability detection
- Performance bottleneck identification
- Code style and best practices enforcement
- Personalized feedback based on developer skill level

## Tech Stack

- Backend: Python FastAPI
- Frontend: React with TypeScript
- Database: PostgreSQL
- AI: OpenAI GPT-4
- DevOps: Docker, GitHub Actions

## Prerequisites

- Docker and Docker Compose
- Node.js 18+
- Python 3.11+
- OpenAI API Key
- GitHub App credentials

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd ai-code-review
```

2. Create a `.env` file in the root directory with the following variables:
```
OPENAI_API_KEY=your_openai_api_key
GITHUB_APP_ID=your_github_app_id
GITHUB_APP_PRIVATE_KEY=your_github_app_private_key
```

3. Build and start the containers:
```bash
docker-compose up --build
```

The application will be available at:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs

## Development

### Backend Development
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend Development
```bash
cd frontend
npm install
npm start
```

## Project Structure

```
ai-code-review/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── db/
│   │   ├── models/
│   │   ├── services/
│   │   └── utils/
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── utils/
│   │   ├── hooks/
│   │   └── context/
│   └── Dockerfile
├── docker-compose.yml
└── README.md
```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT 