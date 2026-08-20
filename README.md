Dockerized Model Server
A containerized team server that runs a small language model and can be published through GitHub Container Registry (GHCR).
Team Members
Wasan
Norah
Hura
What This Project Does
This project packages a Python server and a language model into a Docker image.
The server provides:
/ — lists all team members.
/generate — generates a response using Qwen3-0.6B.
The Docker image is built automatically using GitHub Actions and published to GitHub Container Registry.
Project Structure
dockerized-model/
├── Dockerfile
├── server.py
├── requirements.txt
├── .dockerignore
└── .github/
    └── workflows/
        └── docker-publish.yml
Docker Image
The image is published to GHCR as:
ghcr.io/alshahraninor20-byte/dockerized-model:latest
Run the Published Image
Pull the latest image:
docker pull ghcr.io/alshahraninor20-byte/dockerized-model:latest
Run the server:
docker run -d --name team-server -p 8000:8000 ghcr.io/alshahraninor20-byte/dockerized-model:latest
Test the Server
Check the team members:
curl -s localhost:8000/
Generate a response from the language model:
curl -s localhost:8000/generate
Docker Logs
To see what the server is doing:
docker logs team-server
Stop the container:
docker stop team-server
Dockerfile
The Dockerfile uses a lightweight Python base image rather than ubuntu:latest.
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "server.py"]
GitHub Actions
Every push to the main branch triggers a GitHub Actions workflow that:
Checks out the repository.
Logs in to GHCR using GITHUB_TOKEN.
Builds the Docker image.
Pushes the image to GHCR.
This allows other users to pull and run the team’s server without needing to build the image themselves.
Model
The server uses:
Qwen/Qwen3-0.6B
The model is loaded when the server starts and is used by the /generate endpoint.
Notes
The project does not use a volume mount (-v). The application code is copied into the Docker image during the build process.
Therefore, changes to the source code require rebuilding the image before they appear in a newly started container.
