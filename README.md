# 🚀 FastAPI CI/CD Demo

A hands-on demo project showcasing **FastAPI** with a complete **CI/CD pipeline** using **GitHub Actions**, **Docker**, **GitHub Container Registry (GHCR)**, **Docker Hub**, and **Railway** for deployment.  
This project is built as a **learning resource for DevOps practices**—covering the full journey from writing code to automated deployment.


## 📚 DevOps Learning Outcomes

By completing this project, you will learn:

1. **Version Control with Git & GitHub**  - Manage code changes and collaborate using Git.
   
2. **Automate Testing with GitHub Actions (CI)** - Run tests automatically on every push or pull request.
   
3. **Build & Push Docker Images to Multiple Registries** - Publish to **GHCR** and **Docker Hub** for flexible deployments.
   
4. **Separate CI and CD Pipelines for Clarity** - Keep testing and deployment workflows independent for reliability.
   
5. **Securely Manage Credentials with GitHub Secrets** - Store Docker and registry credentials without exposing them in code.
   
6. **Run Containers Anywhere** - Deploy and run the same application on **Linux, macOS, or Windows** without code changes.
   
7. **Understand Local vs. Containerized Execution** - Learn the difference between running your app locally and inside a Docker container.
   
8. **Expose API Documentation Automatically** - Use FastAPI's built-in **Swagger UI** and **OpenAPI** for instant API docs.
   
9. **Deploy to a Cloud Hosting Platform (Railway)** - Demonstrate how to take a containerized app live with free cloud hosting.

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
 
**Deployment:**
-  Railway – Automated deployments from GitHub with Docker support, public URL generation, and free tier hosting (no credit card required).
 
## 🔍 What These Tools Do in This Project

This project combines several technologies and platforms, each playing a specific role in building, testing, packaging, and deploying the FastAPI application.

---

### **1. FastAPI**
- **Purpose:** Backend web framework for building high-performance APIs in Python.  
- **Role in Project:** Handles API endpoints, request/response validation, and automatic Swagger/OpenAPI documentation.

---

### **2. Docker**
- **Purpose:** Containerization platform that packages applications with all dependencies so they run the same everywhere.  
- **Role in Project:**  
  - Packages the FastAPI app into a portable Docker image.  
  - Ensures consistent environments for local testing, CI/CD builds, and production deployment.

---

### **3. Git & GitHub**
- **Purpose:** Version control and remote repository hosting.  
- **Role in Project:**  
  - Tracks code changes.  
  - Triggers automated workflows via GitHub Actions when changes are pushed.

---

### **4. GitHub Actions (CI/CD)**
- **Purpose:** Automate software workflows such as building, testing, and deployment.  
- **Role in Project:**  
  - **CI (Continuous Integration):** Runs tests on every push or pull request.  
  - **CD (Continuous Delivery):** Builds Docker images and pushes them to Docker Hub & GHCR.

---

### **5. GHCR (GitHub Container Registry) & Docker Hub**
- **Purpose:** Cloud registries for storing and distributing Docker images.  
- **Role in Project:**  
  - Store built images so they can be pulled anywhere without rebuilding from source.

---

### **6. Railway**
- **Purpose:** Cloud hosting platform that supports Docker-based deployments directly from GitHub.  
- **Role in Project:**  
  - Deploys the Dockerized FastAPI app automatically after a GitHub push.  
  - Provides a public URL for accessing the running API.  

---

### **7. pytest & httpx**
- **Purpose:** Testing framework (`pytest`) and HTTP client (`httpx`) for API test automation.  
- **Role in Project:**  
  - Validate API responses before deployment.  
  - Ensure changes don’t break existing functionality.

 
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

---

**UI:**

<img width="1512" height="754" alt="Screenshot 2025-09-02 at 17 34 51" src="https://github.com/user-attachments/assets/ae3d9fb3-87e7-4eec-8752-c3cd6c8c8eda" />


## ✅ Advantages of This Setup

- **Fully Automated CI/CD** — Every code push triggers testing, building, and deployment without manual steps.
- **Multi-Registry Support** — Docker images are pushed to both **Docker Hub** and **GHCR**, giving flexibility in where you pull from.
- **Cross-Platform Ready** — The same Docker image runs on Linux, macOS, or Windows without code changes.
- **Built-in API Documentation** — FastAPI automatically provides Swagger UI and OpenAPI docs.
- **Secure Secrets Management** — GitHub Actions stores all credentials (tokens, passwords) in encrypted secrets.

  
## 🌎 Deployment Options

This setup is highly flexible and can be deployed to:
- **Kubernetes** (Minikube for local or Cloud-managed clusters like GKE, AKS, EKS)
- **AWS ECS / Fargate**
- **Azure Container Apps**
- **Google Cloud Run**
- **Railway** (Free Docker hosting)
- **Any VPS or server** with Docker installed

## 🚀 Future Enhancements

- **Kubernetes Deployment** — Create manifests or Helm charts for container orchestration.
- **Helm Integration** — Package Kubernetes deployments for easy reusability.
- **Staging & Production Environments** — Use GitHub Actions Environments for controlled releases.
- **Monitoring & Logging** — Integrate Prometheus, Grafana, and Loki for observability.
- **Automated Security Scans** — Add container vulnerability scanning in CI.

## 📚 References / Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Docker Documentation](https://docs.docker.com/)
- [Railway Deployment Docs](https://docs.railway.app/)
- [GitHub Container Registry Docs](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry)
