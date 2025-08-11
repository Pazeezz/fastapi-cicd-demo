# 🚀 FastAPI CI/CD Demo

A demo project showcasing FastAPI with a complete CI/CD pipeline using GitHub Actions, Docker, GHCR, and Docker Hub.
This project is designed as a learning resource for DevOps practices in building, testing, containerizing, and deploying a web service.


## 📚 DevOps Learning Outcomes
By completing this project, you will learn how to:

    1. Version control your code with Git & GitHub.

    2. Automate testing with GitHub Actions (CI).

    3. Build & push Docker images to multiple registries (GHCR + Docker Hub).

    4. Separate CI and CD workflows for clarity and reliability.

    5. Use GitHub secrets to store credentials securely.

    6. Run containers anywhere (Linux, macOS, Windows) without code changes.

    7. Understand the difference between running locally vs. running from a Docker image.

    8. Expose API documentation automatically using FastAPI’s Swagger UI.


## 🛠 Tech Stack

**Backend Framework:** 
-  FastAPI (Python 3.11)

**Testing:**
-  pytest
-  httpx (for HTTP request testing)

**Containerization:**
-  Docker
-  Multi-registry publishing (GHCR + Docker Hub)

**CI/CD:**
-  GitHub Actions
    - **CI:** Runs tests on each push/PR
    - **CD:** Builds Docker image and pushes to registries

 
## ⚙️ CI/CD Workflow

**Simplified Flow:**

```bash
GitHub Repo
   ↓
GitHub Actions (CI)
   - Run tests
   - On success → Trigger CD
   ↓
GitHub Actions (CD)
   - Build Docker image
   - Push to GitHub Container Registry (GHCR)
   - Push to Docker Hub
   ↓
Run Anywhere (docker pull & docker run)
```
## 📄 CI Workflow (.github/workflows/ci.yml)

-  Trigger: On push or pull_request

-  Steps:

        1. Checkout code
        2. Setup Python 3.11
        3. Install dependencies
        4. Run tests with pytest


## 📄 CD Workflow (.github/workflows/cd.yml)

-  Trigger: On successful CI workflow

-  Steps:

        1. Checkout the exact commit tested in CI
        2. Login to GHCR and Docker Hub
        3. Generate Docker image metadata (tags & labels)
        4. Build and push to both registries
## 📥 Installation & Local Setup

-  Step-by-step instructions for cloning and running locally without Docker.

-  Good for showing difference between `uvicorn` local run vs Docker run.

```bash
git clone https://github.com/Pazeezz/fastapi-cicd-demo.git

cd fastapi-cicd-demo

pip install -r requirements.txt

uvicorn app.main:app --reload

```
## 🐳 Docker

-  **Build Locally**

```bash
docker build -t fastapi-cicd-demo .

docker run -p 8000:8000 fastapi-cicd-demo
```

-  **Run from Docker Hub**

```bash
docker pull pasindulj/fastapi-cicd-demo:latest

docker run -p 8000:8000 pasindulj/fastapi-cicd-demo:latest
```

-  **Run from GHCR (Private/Public Repo)**

```bash
docker login ghcr.io -u <your-username>

docker pull ghcr.io/<your-username>/fastapi-cicd-demo:latest

docker run -p 8000:8000 ghcr.io/<your-username>/fastapi-cicd-demo:latest

```
## 🧪 Running Tests

-  Show how to manually run tests locally.

```bash
pytest -q
```
## 🔑 Secrets Used in GitHub Actions

-  Clearly list what secrets are needed:

    -  `DOCKERHUB_USERNAME`

    -  `DOCKERHUB_TOKEN`

    -  (Optional) GHCR token if private
## 📡 API Endpoints

Swagger UI: http://localhost:8000/docs

OpenAPI JSON: http://localhost:8000/openapi.json


| Method | Endpoint     | Description                |
| :-------- | :------- | :------------------------- |
| `GET` | `/` | 	Root endpoint (health check) |
| `GET` | `/greet?name=<your-name>` | Returns a greeting message |
| `GET` | `/version` | Shows current app version & Git commit SHA |
| `GET` | `/ui` | Custom HTML UI page |
| `GET` | `/favicon.ico` | Favicon resource |

#### 
## 🖼 Example Run

**Swagger UI:**

<img width="1512" height="750" alt="Screenshot 2025-08-11 at 10 26 54" src="https://github.com/user-attachments/assets/1820a41b-309c-4d0e-a28c-44ac38ae1a4d" />


## ✅ Advantages of This Setup

-  Fully automated CI/CD pipeline for quick deployments.

-  Multi-registry support for flexibility in hosting images.

-  Cross-platform support — Run the same container anywhere.

-  Automated documentation via FastAPI.
## 🌎 Deployment Options

-  Mention that this can be deployed to **Kubernetes, AWS ECS, Azure Container Apps**, or any server with **Docker.**
## 🚀 Future Enhancements

-  Deploy to Kubernetes (Minikube or cloud-managed)

-  Integrate Helm charts for deployment

-  Use GitHub Actions Environments for staging/production


## 📚 References / Resources

-  Links to FastAPI docs, GitHub Actions docs, Docker docs.
