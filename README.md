The primary goal of this project was to transition a 3-tier web application from a standard local development setup into a modern, automated DevOps delivery pipeline. Instead of relying on manual deployment steps, this project establishes a complete end-to-end continuous integration and container orchestration workflow that automatically packages, stores, and prepares updated application code for deployment whenever changes are made.

The 3-Tier web application is a simple website whcih adds different tasks to a list of Tasks. The web application is very simple and the project is not focused on the functionality and User interface of the website, but rather the devOps part of it. The CI/CD pipelines used in it .


The architecture is divided into three distinct functional tiers, all managed and orchestrated locally inside a Kubernetes cluster:

# 1. Frontend Tier:-
Built as an interactive web interface using HTML and served via an Nginx web server.
Acts as the entry point for end-user interactions, sending client requests downstream to the API layer.

# 2. Backend Tier:
Powered by a Python FastAPI REST framework.
Handles business logic, processes incoming API requests from the frontend, and manages communication with the database.

#3. Database Tier:
Utilizes PostgreSQL for persistent data storage.
Leverages Kubernetes Persistent Volumes to ensure data remains intact and persistent across pod restarts or redeployments.


The highlight of this project is its fully automated delivery pipeline, which connects code changes to container registries and cluster deployments:

Source Control & Automation Engine: Hosted on GitHub and powered by GitHub Actions. Pushing code updates to the main branch automatically triggers the pipeline workflow.

Automated Image Build & Security: The pipeline securely authenticates with Docker Hub using encrypted repository secrets, builds isolated container images for both the frontend and backend services, and tags them for release.

Registry Management: The fresh container images are published directly to a public Docker Hub registry, serving as a single source of truth for deployment images.

Container Orchestration & IaC: The underlying Kubernetes cluster infrastructure, deployment manifests, environment variables, and network services are declared programmatically using Terraform, ensuring consistent, reproducible environment provisioning.


This project was divided into 4 phases namely -

1. Phase 1 - Local Containerization - Goal - Turning code into portable and immutable packages and network them locally.
This included -
a. Building a functional 3-Tier File system architecture
b. Write optimized Dockerfiles using proper caching layers
c. Launch all tiers with a single command via Docker Compose

2. Phase 2 - Local Orchestration with Kuberenetes - Goal - Transition from basic conatiners to production-grade orchestration. Kubernetes was used to manage, automate deployment, scaling and operation of containerized applications.

3. Phase 3 - Infrastructure as Code (IaC) - Automate the creation of physical cloud environments using software code

4. Phase 4 - Automated GitOps CI/CD Pipeline - Goal - Achieve continuos delivery Automation




Stack Used 

Frontend Tier: HTML, CSS, Nginx

Backend Tier: Python (FastAPI)

Database Tier: PostgreSQL (with Kubernetes Persistent Volumes)

Containerization & Registry: Docker, Docker Hub

Orchestration & Infrastructure: Kubernetes (Minikube), Terraform (IaC)

CI/CD Pipeline: GitHub Actions

Version Control: Git, GitHub


