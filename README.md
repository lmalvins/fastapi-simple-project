# FastAPI Simple Project

A lightweight, modular FastAPI project using **Poetry** and a **Hexagonal Architecture** approach for clean separation of concerns.

---

##  Features

- FastAPI as the web framework
- Hexagonal architecture (domain, application, infrastructure layers)
- Pytest for testing
- SQLAlchemy ready (DB adapter)
- Dependency management via Poetry

---

##  Pre-requisites

Before getting started, make sure you have:

- Python **3.11**
- [Poetry](https://python-poetry.org/docs/#installation) installed  
  _(Recommended install method: `brew install poetry` or use the official installer)_

```bash
# Install Poetry (if not already)
brew install poetry
# OR
curl -sSL https://install.python-poetry.org | python3 -
```

## 🚀 Running the Application

After installing dependencies, you can start the FastAPI server using **Uvicorn**.

### 1. Install dependencies

If you haven’t already, run:

```bash
poetry install
```

### 2. Start the server

Run the following command from the project root:
```bash
PYTHONPATH=src uvicorn main:app --reload
```
- PYTHONPATH=src ensures that internal modules (like api, services, etc.) are correctly resolved.
- --reload enables automatic reload on code changes (useful during development).

The app will be available at:
- http://127.0.0.1:8000
- Swagger UI: http://127.0.0.1:8000/docs
- Redoc: http://127.0.0.1:8000/redoc