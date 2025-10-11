# Backend Production Dockerfile
FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy application code
COPY . .

# Install pre-built clinical_trials_client wheel from artifact
COPY build_wheels/ /tmp/wheels/
RUN pip install /tmp/wheels/*.whl

# Create non-root user
RUN useradd -m -s /bin/bash appuser && \
    chown -R appuser:appuser /app
USER appuser

# Expose port
EXPOSE 8000

# Default command - production server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]