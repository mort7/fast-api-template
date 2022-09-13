# FastAPI Template
Template repository for quickly building python applications with [FastAPI](https://fastapi.tiangolo.com/)

## Features
- Dockerfile
- Redis Connection

# Setup
## Install dependencies
```
poetry install
```

# Formatting and Linting
## Black - Formatting
```
black app
```

## Pylint - Linting
```
pylint --disable=E0401 --extension-pkg-whitelist='pydantic' app
```

# Running Application
## Local Devlopment - Reload on Save (Runs on port 8000)
```
uvicorn app.main:app --reload
```

## Uvicorn
```
uvicorn app.main:app --host 0.0.0.0 --port 5000
```

## Gunicorn
```
gunicorn --bind=0.0.0.0 --workers=4 --worker-class=uvicorn.workers.UvicornWorker app.main:app
```