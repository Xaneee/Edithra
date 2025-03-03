#!/bin/bash

# 🚀 Edithra Automated AWS Deployment Script (LOCAL BUILD)
# This script will set up an AWS EC2 instance, install Docker, and deploy Edithra locally

echo "🔹 Step 1: Updating System Packages"
sudo apt update && sudo apt upgrade -y

echo "🔹 Step 2: Installing Required Dependencies"
sudo apt install -y docker.io docker-compose unzip awscli curl

echo "🔹 Step 3: Starting Docker"
sudo systemctl start docker
sudo systemctl enable docker

echo "🔹 Step 4: Creating Required Directories"
mkdir -p ~/edithra
cd ~/edithra

echo "🔹 Step 5: Creating Docker Compose File"

cat <<EOL > docker-compose.yml
version: '3.8'

services:
  backend:
    build: 
      context: .
      dockerfile: backend/Dockerfile
    container_name: edithra_backend
    ports:
      - "8000:8000"
    env_file:
      - .env
    depends_on:
      - db
      - redis

  frontend:
    build: 
      context: .
      dockerfile: frontend/Dockerfile
    container_name: edithra_frontend
    ports:
      - "3000:3000"
    depends_on:
      - backend

  db:
    image: postgres:latest
    container_name: edithra_db
    environment:
      POSTGRES_USER: edithra_user
      POSTGRES_PASSWORD: securepassword
      POSTGRES_DB: edithra_db
    ports:
      - "5432:5432"
    volumes:
      - db_data:/var/lib/postgresql/data

  redis:
    image: redis:latest
    container_name: edithra_cache
    ports:
      - "6379:6379"

  nginx:
    image: nginx:latest
    container_name: edithra_nginx
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
    depends_on:
      - backend
      - frontend

volumes:
  db_data:
EOL

echo "🔹 Step 6: Creating Nginx Configuration"
cat <<EOL > nginx.conf
events {}

http {
    server {
        listen 80;
        location / {
            proxy_pass http://edithra_frontend:3000;
        }
        location /api/ {
            proxy_pass http://edithra_backend:8000/;
        }
    }
}
EOL

echo "🔹 Step 7: Setting Up Environment Variables"
cat <<EOL > .env
OPENAI_API_KEY=your_openai_api_key
DATABASE_URL=postgresql://edithra_user:securepassword@db/edithra_db
REDIS_URL=redis://redis:6379/0
STRIPE_SECRET_KEY=your_stripe_secret_key
EOL

echo "🔹 Step 8: Building Docker Images Locally"

# Build Backend
echo "🔹 Building Backend Image"
docker build -t edithra-backend -f backend/Dockerfile .

# Build Frontend
echo "🔹 Building Frontend Image"
docker build -t edithra-frontend -f frontend/Dockerfile .

echo "🔹 Step 9: Deploying Edithra Services"
sudo docker-compose up -d

echo "🎉 Deployment Complete! Edithra is now running on AWS"
