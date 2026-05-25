# EduFlow – CI/CD Pipeline Proof of Concept

A Flask-based E-Learning REST API with a fully automated CI/CD pipeline using GitHub Actions, Docker, and a self-hosted deployment runner. Built as a university DevOps case study.

## Overview

EduFlow is a fictional EdTech startup serving ~40,000 students with exam-preparation modules. This Proof of Concept replaces a manual FTP-based deployment process (4.5 hours per release, 23% failure rate) with an automated CI/CD pipeline targeting DORA High-Performer metrics.

## Tech Stack

| Component         | Technology                          |
|--------------------|-------------------------------------|
| Application        | Python 3.12 / Flask 3.0             |
| Testing            | pytest (Unit + Integration)         |
| Containerization   | Docker (python:3.11-slim)           |
| Container Registry | Docker Hub (private repository)     |
| CI/CD Engine       | GitHub Actions                      |
| Deployment Server  | Ubuntu 24.04 VM (VirtualBox)        |
| Runner             | Self-hosted GitHub Actions Runner   |

## Pipeline Architecture

```
Code Push → GitHub
       │
       ▼
┌──────────────────────────────────────┐
│  1. TEST (GitHub-hosted Runner)      │
│     pytest: 2 unit + 5 integration   │
└──────────────┬───────────────────────┘
               ▼
┌──────────────────────────────────────┐
│  2. BUILD & PUSH (GitHub-hosted)     │
│     Docker build → Docker Hub        │
│     Tags: latest + git SHA           │
└──────────────┬───────────────────────┘
               ▼
┌──────────────────────────────────────┐
│  3. DEPLOY STAGING (Self-hosted)     │
│     Pull image → Run on port 5001   │
└──────────────┬───────────────────────┘
               ▼
       ┌───────────────┐
       │ Manual Approval│
       │   (GitHub UI)  │
       └───────┬───────┘
               ▼
┌──────────────────────────────────────┐
│  4. DEPLOY PRODUCTION (Self-hosted)  │
│     Pull image → Run on port 5000   │
└──────────────────────────────────────┘
```

**Key design decisions:**
- Dual tagging (`latest` + SHA) enables rollback to any specific build
- Manual approval gate separates staging validation from production release
- Self-hosted runner on the VM handles both staging and production deployments

## API Endpoints

| Method | Endpoint          | Description                  |
|--------|-------------------|------------------------------|
| GET    | `/`               | App info and status          |
| GET    | `/health`         | Health check                 |
| GET    | `/courses`        | List all courses             |
| GET    | `/courses/<id>`   | Get course by ID (404 if N/A)|

## Getting Started

### Prerequisites

- Python 3.12+
- Docker Desktop (Windows/Mac) or Docker Engine (Linux)
- Git

### Local Setup

```bash
# Clone the repository
git clone https://github.com/Travelcookie/EduFlow.git
cd EduFlow

# Create virtual environment and install dependencies
python -m venv venv
source venv/bin/activate        # Linux/Mac
# venv\Scripts\activate         # Windows
pip install -r requirements.txt

# Run the application
python app.py
# → http://localhost:5000
```

### Run with Docker

```bash
docker build -t eduflow-app .
docker run -p 5000:5000 eduflow-app
```

## Running Tests

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=app

# Run only unit tests
pytest tests/test_unit.py

# Run only integration tests
pytest tests/test_integration.py
```

The test suite includes 7 tests: 2 unit tests (data structure validation) and 5 integration tests (HTTP endpoint verification).

## Project Structure

```
eduflow-app/
├── app.py                  # Flask application
├── requirements.txt        # Python dependencies
├── Dockerfile              # Container configuration
├── .dockerignore            # Files excluded from Docker image
├── .gitignore               # Files excluded from Git
├── tests/
│   ├── __init__.py
│   ├── test_unit.py         # Unit tests (business logic)
│   └── test_integration.py  # Integration tests (API endpoints)
└── .github/
    └── workflows/
        └── ci-cd.yml        # GitHub Actions pipeline definition
```

## Academic Context

This project was developed as a case study for a DevOps university course. It demonstrates the end-to-end implementation of a CI/CD pipeline, evaluated against DORA metrics (Deployment Frequency, Lead Time, MTTR, Change Failure Rate). The pipeline reduced deployment time from 4.5 hours to under 15 minutes and eliminated manual deployment errors.

---

*Built with Flask, tested with pytest, shipped with GitHub Actions.*
