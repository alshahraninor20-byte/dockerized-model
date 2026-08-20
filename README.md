🤖 Dockerized Model Server
A lightweight, reproducible AI server — built with Docker and published through GitHub Container Registry.
This project demonstrates how to package a Python server together with a language model into a Docker image, automatically build and publish it through GitHub Actions, and make it runnable with a single command.


⸻


✨ Overview
The server combines a simple HTTP API with Qwen3-0.6B, allowing users to interact with a language model through a containerized endpoint.
The application is designed to be:
🐳 Containerized — the application and its dependencies live inside the image.
🔁 Reproducible — anyone can run the same published image.
⚙️ Automated — GitHub Actions builds and publishes the image.
🌍 Portable — no local project setup is required to run the published image.


⸻


👥 Team
Member
Wasan
Norah
Hura


⸻
## 🏗️ Architecture

```text
                    GitHub Repository
                           │
                           ▼
                    GitHub Actions
                           │
                           ▼
                     Docker Build
                           │
                           ▼
              GitHub Container Registry
                           │
                           ▼
                    Docker Pull / Run
                           │
                           ▼
                    ┌──────────────┐
                    │    Server    │
                    │    :8000     │
                    └──────┬───────┘
                           │
                  ┌────────┴────────┐
                  │                 │
                  ▼                 ▼
                 `/`          `/generate`
                  │                 │
                  ▼                 ▼
           Team Information     Qwen3-0.6B
                                      │
                                      ▼
                              Generated Response
⸻


dockerized-model/
│
├── .github/
│   └── workflows/
│       └── docker-publish.yml
│
├── .dockerignore
├── Dockerfile
├── requirements.txt
├── server.py
└── README.md
⸻


🧠 Language Model
The server uses:
Qwen3-0.6B
Qwen/Qwen3-0.6B
The model is loaded when the container starts and is accessed through the /generate endpoint.


⸻


🚀 Run the Published Image
You don’t need to clone the repository or build the image yourself.
1. Pull the image
docker pull ghcr.io/alshahraninor20-byte/dockerized-model:latest
2. Start the server
docker run -d \
  --name team-server \
  -p 8000:8000 \
  ghcr.io/alshahraninor20-byte/dockerized-model:latest
That’s it. The server is now running locally on port 8000.


⸻


🔎 API Endpoints
GET /
Returns the team members.
curl -s localhost:8000/
Example:
Team members: Wasan, Norah, Hura


⸻


GET /generate
Sends a prompt to the language model and returns its generated response.
curl -s localhost:8000/generate
Example response:
{
  "prompt": "Give me a short introduction to large language models.",
  "response": "..."
}


⸻


🐳 Docker
The application is built from a lightweight Python image:
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "server.py"]
Why 
python:3.12-slim
?
Instead of starting from ubuntu:latest, the project uses a lightweight Python image that already provides the required Python runtime while keeping the base image smaller.


⸻


🔄 Continuous Deployment
Every push to the main branch triggers the GitHub Actions workflow.
Push to main
     │
     ▼
GitHub Actions
     │
     ▼
Build Docker Image
     │
     ▼
Push to GHCR
     │
     ▼
Published :latest Image
The workflow uses GitHub’s built-in GITHUB_TOKEN to authenticate with GHCR.


⸻


📦 Container Registry
Published image:
ghcr.io/alshahraninor20-byte/dockerized-model:latest
The image is publicly available so users can pull and run the team’s server without logging into a registry.


⸻


🧪 Useful Commands
View running containers
docker ps
View logs
docker logs team-server
Stop the server
docker stop team-server
View images
docker images


⸻


💡 Key Concept
Unlike a development setup using a volume mount:
-v
this project copies the application code into the Docker image itself.
Therefore, changing the source code does not change an already-built image.
