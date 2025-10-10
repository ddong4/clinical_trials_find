# Development Setup

## Quick Start

1. **Start all services:**
   ```bash
   docker compose up --build
   ```

2. **Access your applications:**
   - 🚀 **FastAPI Backend**: http://localhost:4682
   - 📖 **Swagger UI**: http://localhost:4682/docs
   - 🎨 **Streamlit Frontend**: http://localhost:6084

## Development Workflow

### Using VS Code Tasks (Optional)
- **Start Services**: `Ctrl+Shift+P` → "Tasks: Run Task" → "Docker Compose Up"
- **Stop Services**: `Ctrl+Shift+P` → "Tasks: Run Task" → "Docker Compose Down"
- **Restart Backend**: `Ctrl+Shift+P` → "Tasks: Run Task" → "Restart Backend Service"
- **View Logs**: `Ctrl+Shift+P` → "Tasks: Run Task" → "View Backend Logs"

### Manual Commands
```bash
# Start all services
docker compose up --build

# Stop all services
docker compose down

# Restart specific service
docker compose restart backend
docker compose restart frontend

# View logs
docker compose logs -f backend
docker compose logs -f frontend

# Rebuild and restart
docker compose up --build --force-recreate
```

## Hot Reload
- **Backend**: FastAPI runs with `--reload` flag, so changes to `.py` files will automatically restart the server
- **Frontend**: Streamlit automatically detects changes and prompts to rerun

## File Structure
```
├── backend/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app/
│       └── main.py
├── frontend/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── streamlit_app/
│       └── main.py
├── docker-compose.yml
└── .vscode/
    ├── settings.json
    ├── extensions.json
    └── tasks.json
```

## Ports
- Backend (FastAPI): 4682 → 8000 (container)
- Frontend (Streamlit): 6084 → 8501 (container)