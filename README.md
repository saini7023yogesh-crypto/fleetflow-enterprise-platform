# fleetflow-enterprise-platform

Enterprise Order Processing Platform with Automated CI/CD





\# FleetFlow Enterprise Platform



A containerized backend application demonstrating modern DevOps practices using Docker, GitHub Actions, Kubernetes, and automated security scanning.



\## Project Overview



FleetFlow Enterprise Platform is a backend application built with \*\*FastAPI and PostgreSQL\*\*, designed to demonstrate how a modern application can be developed, tested, containerized, and deployed using DevOps tools and workflows.



The main objective of this project is to implement a practical CI pipeline, automate application quality and security checks, publish Docker images, and deploy the application on Kubernetes.



This project is part of a hands-on Cloud and DevOps engineering learning journey.



\## Project Objectives



\- Build a backend application using FastAPI.

\- Integrate PostgreSQL for persistent data storage.

\- Containerize the application using Docker.

\- Use Docker Compose for local application and database orchestration.

\- Automate testing and code-quality checks using GitHub Actions.

\- Scan application files and container configurations for security issues using Trivy.

\- Build and publish Docker images to GitHub Container Registry (GHCR).

\- Deploy the application and database on Kubernetes.

\- Configure Kubernetes health probes, resource limits, persistent storage, and security contexts.



\## Technology Stack



| Category | Technologies |

|---|---|

| Backend | Python, FastAPI |

| Database | PostgreSQL |

| Containerization | Docker, Docker Compose |

| CI/CD | GitHub Actions |

| Container Registry | GitHub Container Registry (GHCR) |

| Orchestration | Kubernetes, kubectl |

| Testing | Pytest |

| Code Quality | Ruff |

| Security Scanning | Trivy |

| Version Control | Git, GitHub |



\## Architecture



The project follows this workflow:



1\. Application code is maintained in GitHub.

2\. GitHub Actions runs automated checks and tests.

3\. Trivy performs security scanning.

4\. Docker builds the application image.

5\. The image is published to GHCR.

6\. Kubernetes runs the application and PostgreSQL using Deployments and Services.

7\. Kubernetes health probes monitor application availability.



\## Key Features



\### Application

\- REST API built with FastAPI.

\- PostgreSQL database integration.

\- CRUD operations.

\- Automated application tests.



\### Docker

\- Custom Dockerfile.

\- Docker Compose configuration.

\- Containerized application environment.



\### Continuous Integration

\- Automated GitHub Actions workflow.

\- Python code-quality checks using Ruff.

\- Automated tests using Pytest.

\- Security scanning using Trivy.

\- Docker image publishing to GHCR.



\### Kubernetes

\- Application and PostgreSQL Deployments.

\- Kubernetes Services.

\- Persistent Volume Claim for database storage.

\- Kubernetes Secrets for database configuration.

\- Startup, readiness, and liveness probes.

\- CPU and memory requests and limits.

\- Container security contexts.



\## Repository Structure



```text

fleetflow-enterprise-platform/

│

├── .github/

│   └── workflows/

│       └── ci.yml

│

├── k8s/

│   ├── fleetflow.yaml

│   └── api-health-patch.yaml

│

├── Dockerfile

├── docker-compose.yml

├── requirements.txt

├── README.md

└── application source and test files

```



\## Running the Application



\### Prerequisites



\- Python

\- Docker

\- Docker Compose

\- Git



\### Clone the Repository



```bash

git clone https://github.com/saini7023yogesh-crypto/fleetflow-enterprise-platform.git



cd fleetflow-enterprise-platform

```



\### Start the Application



```bash

docker compose up --build

```



\### Access API Documentation



Once the application is running, open:



```text

http://localhost:8000/docs

```



\## Kubernetes Deployment



A local Kubernetes environment such as Docker Desktop Kubernetes is used for deployment and testing.



Apply the Kubernetes manifests:



```bash

kubectl apply -f k8s/fleetflow.yaml

```



Check the running Pods:



```bash

kubectl get pods

```



Check Kubernetes Services:



```bash

kubectl get services

```



\## Project Status



\*\*Completed implementation:\*\*

\- Backend application and PostgreSQL integration.

\- Docker and Docker Compose setup.

\- Automated CI workflow.

\- Testing, code quality, and security scanning.

\- Docker image publishing to GHCR.

\- Kubernetes application deployment and configuration.



\*\*Future improvements:\*\*

\- Automated deployment (CD) from GitHub Actions to Kubernetes.

\- Deployment health verification through the CI/CD workflow.

\- Cloud infrastructure deployment and monitoring.



\## Learning Outcomes



This project provides practical experience with:



\- Containerization and application deployment.

\- CI workflow automation.

\- Automated testing and security scanning.

\- Docker image management.

\- Kubernetes workloads and services.

\- Persistent storage and application health management.

\- Git-based development workflows.



\## Author



\*\*Yogesh Kumar\*\*



AWS Certified Solutions Architect – Associate



Interested in Cloud Engineering, DevOps, Automation, and Cloud Infrastructure.



\---



\*This is a hands-on portfolio project developed to demonstrate practical Cloud and DevOps engineering skills.\*

