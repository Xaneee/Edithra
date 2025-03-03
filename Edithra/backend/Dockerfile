# Use Python 3.9 with essential libraries
FROM python:3.9-slim AS base

# Set the working directory
WORKDIR /app

# Install system dependencies for AI, PostgreSQL, and Redis
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libsm6 \
    libxext6 \
    libgl1 \
    build-essential \
    postgresql-client \
    redis-tools \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the backend code
COPY ./Edithra/backend /app/backend

# Set PYTHONPATH so FastAPI can find modules
ENV PYTHONPATH=/app

# Copy environment variables
COPY .env /app/.env

# Expose the required 6 ports
EXPOSE 80 443 8000 6379 5432 22


# Start FastAPI app
CMD ["uvicorn", "backend.Edithra_backend:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]


