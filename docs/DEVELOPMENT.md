# Development Setup

## Prerequisites
- VSCode preferred (have suggested extensions and tasks)
- Docker Desktop

## Quick Start

### Development Mode (with hot reload)
1. **Start all services:**
   ```bash
   docker compose up --build
   ```

## Docker Structure

### Development Files
- `backend/Dockerfile.dev` - Development backend with volume mounts
- `frontend/Dockerfile.dev` - Development frontend with volume mounts
- `docker-compose.yml` - Development compose with hot reload

## Development Workflow

### Using VS Code Tasks
- **Start Services**: `Ctrl+Shift+P` → "Tasks: Run Task" → "Docker Compose Up"
- **Stop Services**: `Ctrl+Shift+P` → "Tasks: Run Task" → "Docker Compose Down"
- **Restart Backend**: `Ctrl+Shift+P` → "Tasks: Run Task" → "Restart Backend Service"
- **View Logs**: `Ctrl+Shift+P` → "Tasks: Run Task" → "View Backend Logs"

### Manual Commands
```bash
# Development mode
docker compose up --build
docker compose down

# Production mode  
docker compose -f docker-compose.prod.yml up --build
docker compose -f docker-compose.prod.yml down

# Restart specific service (dev)
docker compose restart backend
docker compose restart frontend

# View logs
docker compose logs -f backend
docker compose logs -f frontend
```

## Hot Reload
- **Development**: Both FastAPI and Streamlit run with hot reload via volume mounts

## File Structure
```
├── backend/
│   ├── Dockerfile          # Production
│   ├── Dockerfile.dev      # Development  
│   ├── requirements.txt
│   ├── .env                # Add your API Keys (like .env.example)
│   └── app/
│       └── main.py
├── frontend/
│   ├── Dockerfile          # Production
│   ├── Dockerfile.dev      # Development
│   ├── requirements.txt
│   └── streamlit_app/
│       └── main.py
├── docker-compose.yml      # Development
└── .vscode/
    ├── settings.json
    ├── extensions.json
    └── tasks.json
```

## CI/CD
The GitHub workflow builds production images from the `Dockerfile` files and pushes them to GitHub Container Registry.