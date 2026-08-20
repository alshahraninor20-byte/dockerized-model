import json
import urllib.request

TEAM = "13"
BY = "Huraa Albrahim"
IMAGE = "ghcr.io/alshahraninor20-byte/dockerized-model:latest"

# 1. Get the real result from your running model
with urllib.request.urlopen("http://localhost:8000/generate") as response:
    result = json.load(response)

# 2. Prepare the data for the board
data = {
    "team": TEAM,
    "by": BY,
    "model": result["model"],
    "image": IMAGE,
    "tokens_per_sec": result["tokens_per_sec"],
    "sample": result["sample"]
}

# 3. Submit it
request = urllib.request.Request(
    "https://aidc.nadir.sh/model",
    data=json.dumps(data).encode(),
    headers={
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0"
    },
    method="POST"
)

with urllib.request.urlopen(request) as response:
    print(response.read().decode())
