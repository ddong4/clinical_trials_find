# Backend Dockerfile
FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /workspace

# Copy and install requirements
COPY requirements.txt /tmp/backend-requirements.txt
RUN pip install --upgrade pip && \
    pip install -r /tmp/backend-requirements.txt

# Install development tools
RUN pip install pylint pytest

# Expose port
EXPOSE 8000

# Default command - start FastAPI dev server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]