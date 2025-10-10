# Development Setup

## Quick Start

### Development Mode (with hot reload)
1. **Start all services:**
   ```bash
   docker compose up --build
   ```

### Production Mode (standalone containers)
1. **Start all services:**
   ```bash
   docker compose -f docker-compose.prod.yml up --build
   ```

2. **Access your applications:**
   - 🚀 **FastAPI Backend**: http://localhost:4682
   - 📖 **Swagger UI**: http://localhost:4682/docs
   - 🎨 **Streamlit Frontend**: http://localhost:6084

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
│   └── app/
│       └── main.py
├── frontend/
│   ├── Dockerfile          # Production
│   ├── Dockerfile.dev      # Development
│   ├── requirements.txt
│   └── streamlit_app/
│       └── main.py
├── docker-compose.yml      # Development
├── docker-compose.prod.yml # Production
└── .vscode/
    ├── settings.json
    ├── extensions.json
    └── tasks.json
```

## CI/CD
The GitHub workflow builds production images from the `Dockerfile` files and pushes them to GitHub Container Registry.