# Docker Tutorial

## Concept

```mermaid
flowchart LR
    subgraph docker_container[Docker Container]
        direction TB
            docker_container1[Docker Container 1] --> docker_container2[Docker Container 2]
            docker_container2 --> docker_container3[Docker Container 3]

            linkStyle 0 stroke:none,stroke-width:0
            linkStyle 1 stroke:none,stroke-width:0
    end

    subgraph file_system[File System]
        direction TB
            docker_area[Docker Area]
    end

    docker_file[Dockerfile] --Build--> docker_image[Docker Image] --Run--> docker_container

    docker_container --bind mount--> file_system
    docker_container --volume--> docker_area
```

* **`Bind mounts`** directly map a file or folder from the host’s filesystem into a container, reflecting host changes immediately
* **`Docker volumes`** are managed by Docker itself in a separate storage area, designed for portability, easier management, and optimized persistent storage

## Code

<details>
    <summary>Extra</summary>

---

## Docker image list
```bash
>>> docker image ls

REPOSITORY    TAG       IMAGE ID       CREATED        SIZE
hello-world   latest    ec153840d1e6   6 months ago   20.4kB
```

## List running containers
```bash
>>> docker ps

CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

## Stop a container using its ID (from docker ps)
```bash
docker stop <container-id>
```

## Delete Docker image
```bash
docker rmi -f <image-id / image-name>
```

## Removes all unused Docker objects

* Removes stopped containers, unused networks, dangling images, and build cache. Does not remove all unused images
```bash
docker system prune
```

* Additionally removes all unused images, not just dangling ones.
```bash
docker system prune -a
```

---

</details>

## 1. Verify Docker Installation
```bash
>>> docker --version

Docker version 28.3.2, build 578ccf6
```

## 2. Pull a Docker Image
```bash
>>> docker pull hello-world

Using default tag: latest
latest: Pulling from library/hello-world
e6590344b1a5: Pull complete
Digest: sha256:ec153840d1e635ac434fab5e377081f17e0e15afab27beb3f726c3265039cfff
Status: Downloaded newer image for hello-world:latest
docker.io/library/hello-world:latest
```

## 3: Run a Container
```bash
>>> docker run hello-world
```

<details>
    <summary>Output</summary>

```bash
Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
1. The Docker client contacted the Docker daemon.
2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
$ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
https://hub.docker.com/

For more examples and ideas, visit:
https://docs.docker.com/get-started/
```
</details>

## 4. Create a Docker Image

<details>
    <summary>dockerfile</summary>

```dockerfile
# Use official lightweight Python 3.12 image as the base image
FROM python:3.12-slim

# Set working directory inside the container to /usr/src/app
WORKDIR /usr/src/app

# Update package lists and install system dependencies required for Python packages and supervisor
# Then clean up apt cache to reduce image size
RUN apt-get update && apt-get install -y \
    && rm -rf /var/lib/apt/lists/*

# Copy the UV binary and related files from the ghcr.io/astral-sh/uv image to /bin/ directory inside the container
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy environment configuration file into the container
COPY .env .

# Copy Python application source code from local ../draft/scr_v2 directory into container
COPY ../draft/scr_v2 .

# Copy Python dependencies list into the container
COPY requirements.txt .

# Use UV's pip wrapper to install Python dependencies listed in requirements.txt with no cache and system-wide
RUN uv pip install --system --no-cache-dir -r requirements.txt

# Expose port 5000 to allow external access to the application
EXPOSE 5000

# Default command to start the Python application
CMD ["python", "app.py"]
```
</details>

## 5: Build a Docker Image
```bash
docker build -f ./Docker/dockerfile -t flask-app .
```

* `-t` flag names the image `flask-app`
* `.` specifies the current directory

## 6: Run Your Custom Container
```bash
docker run -p 5000:5000 flask-app
```

## 7: Build Docker-Compose File

<details>
    <summary>docker-compose.yml</summary>

```dockerfile
version: "3.9"

services:
  flask_test:
    build:
      context: ..
      dockerfile: ./Docker/dockerfile.flask_test
    env_file:
      - ../.env
    ports:
      - "5000:5000"
    # volumes:
    #   - ./draft/scr_v2:/usr/src/app
    restart: unless-stopped

  streamlit_test:
    build:
      context: ..
      dockerfile: ./Docker/dockerfile.streamlit_test
    env_file:
      - ../.env
    ports:
      - "8501:8501"
    # volumes:
    #   - ./draft/scr_v2:/usr/src/app
    restart: unless-stopped
```
</details>

## 8: Build Docker-Compose Image
```bash
docker compose -f ./Docker/docker-compose.yml up
```

## 9. Docker Container with Bind Mount
<details>
    <summary>bindmount-example Dockerfile</summary>

```dockerfile
# Dockerfile for both examples
FROM python:3.10-slim

WORKDIR /app

COPY app.py .

RUN pip install flask

CMD ["python", "app.py"]

```
</details>

```bash
docker build -t bindmount-example .

# Bind mount a host directory './app-data' into the container's /app/data
docker run -d --name bindmount-container -p 5000:5000 -v "$(pwd)/app-data:/app/data" bindmount-example
```

* **Local path:** `$(pwd)/app-data`
* **Container path:** `/app/data`

## 10. Docker Container with Volume
<details>
    <summary>volume-example Dockerfile</summary>

```dockerfile
# Dockerfile for both examples
FROM python:3.10-slim

WORKDIR /app

COPY app.py .

RUN pip install flask

CMD ["python", "app.py"]

```
</details>

```bash
docker build -t volume-example .

# Create docker volume first (optional step, Docker can auto create)
docker volume create my_app_data

# Bind mount a host directory './app-data' into the container's /app/data
docker run -d --name volume-container -p 5000:5000 -v my_app_data:/app/data volume-example
```

* **Volume Name:** `my_app_data`
* **Container path:** `/app/data`
