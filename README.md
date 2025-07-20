## 🚀 DevOps Assignment: Two-Tier Web App (FastAPI + Next.js)

This project demonstrates end-to-end DevOps skills including containerization, CI/CD, infrastructure as code with Terraform, monitoring, security, and load balancing using AWS.


## Project Structure
.
```
.
Devops-Assignment/
│
├── README.md
├── backend/
│   ├── app/                  # FastAPI code
│   ├── tests/                # Pytest unit tests
│   ├── Dockerfile            # DockerFile
│   └── requirements.txt
│
├── frontend/
│   ├── pages/                # Next.js pages
│   ├── tests/                # Cypress or Jest tests
│   ├── Dockerfile            # DockerFile
│   └── package.json
│
├── .github/
│   └── workflows/
│       ├── backend.yml       # CI/CD for backend
│       ├── frontend.yml
│       └── terraform.yml
│
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   └── backend.tf

```

## Branching Strategy
##  Github Flow Branching Strategy

- `main` – Stable, production-ready code.
- `develop` – Integrated feature branches.
- `feature/*` – One branch per feature (e.g. `feature/backend`, `feature/frontend`, `feature/terraform`)
- PRs reviewed before merging to develop, then merged into main for deployment.
---------------------

## Setup Instructions
### Prerequisites
- Docker
- AWS CLI
- Terraform
- Python & Node.js installed

### Steps
1. Clone the repo
2. Navigate to `backend/` and run: `uvicorn app.main:app --reload`
3. Navigate to `frontend/` and run: `npm run dev`
4. Run tests using:
   - Backend: `pytest`
   - Frontend: `npx cypress open`
5. Build Docker images and push to ECR (automated in CI/CD)
--------------------

## CI/CD Pipeline

CI (On develop branch push):

- Checkout code

- Run backend unit tests (Pytest)

- Run frontend E2E tests (Cypress)

- Build Docker images (backend & frontend)

- Tag images with Git SHA

- Push Docker images to AWS ECR (currently failing — WIP to resolve issue)

CD (On main merge):

- Terraform applies infra (ECS, ALB, S3 backend, Cloudwatch)

- Deploy containers to ECS
----------------------

## Infrastructure (Terraform)

Provisioned AWS resources:
- VPC, Subnets, Internet Gateway
- ECS Cluster (Fargate) for frontend & backend
- Application Load Balancer
- S3 Bucket for storing Terraform state
- CloudWatch Dashboard + CPU Alarm
- IAM roles with least privilege
- Secrets in AWS Secrets Manager
------------------------
## 📊 Monitoring

- AWS CloudWatch dashboard shows CPU, memory, and request count.
- Alarm notifies when CPU > 70% for 5 minutes.
---------------------
## Load Balancing

- Application Load Balancer created

- ECS service configured (although app image isn't deployed yet due to ECR push failure)

- Failover test pending successful deployment
----------------------
## Deliverables

- GitHub Repo: https://github.com/UntameBeast/DevOps-Assignment.git 

- Hosted Link (frontend/backend): Pending ECR push fix

Hands-on Evidence:

- Terraform state in S3 ✅

- CloudWatch dashboard & alarms ✅

- IAM & Secrets configuration ✅

- ECR logs showing failed push ❌ (debugging)

- ALB setup exists; load test to follow
------------------------------------------------------
