# Frontend Dockerfile
FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy and install requirements
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expose port
EXPOSE 8501

# Default command (can be overridden in docker-compose)
CMD ["streamlit", "run", "streamlit_app/main.py", "--server.port", "8501", "--server.address", "0.0.0.0"]