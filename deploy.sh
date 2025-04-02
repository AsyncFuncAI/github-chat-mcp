#!/bin/bash
set -e

# Build the Docker image
docker build -t github-chat-mcp .

# Optional: Push to a container registry like Docker Hub or GitHub Container Registry
# docker tag github-chat-mcp yourusername/github-chat-mcp:latest
# docker push yourusername/github-chat-mcp:latest

# Run locally for testing
echo "Starting GitHub Chat MCP server locally for testing..."
docker run -e GITHUB_API_KEY=$GITHUB_API_KEY -p 8000:8000 github-chat-mcp

# Instructions for deploying to production environments
cat << EOF

------------------------------------
Production Deployment Instructions:
------------------------------------

1. Push the Docker image to a container registry:
   docker tag github-chat-mcp yourusername/github-chat-mcp:latest
   docker push yourusername/github-chat-mcp:latest

2. Deploy to your preferred hosting service:
   
   - For AWS ECS:
     aws ecs create-service --service-name github-chat-mcp --task-definition github-chat-mcp --desired-count 1
     
   - For Kubernetes:
     kubectl apply -f kubernetes-deployment.yaml
     
   - For Google Cloud Run:
     gcloud run deploy github-chat-mcp --image yourusername/github-chat-mcp:latest --platform managed
     
3. Configure the environment variable GITHUB_API_KEY in your production environment.

4. Register your MCP with the MCP registry by following the MCP documentation.

EOF 