# Test task:
## Description
Implement django app that will implement the tree menu

### examples:
![screenshot 1](docs/screenshots/screen1.png)

![screenshot 2](docs/screenshots/screen2.png)

## 🚀 Project Setup Guide (local)

This guide will help you set up and run the Django project using the [uv](https://docs.astral.sh/uv/getting-started/installation/) Python package manager and Docker for services like PostgreSQL.

---

### ✅ Prerequisites

- [Python](https://www.python.org/) (3.11+ recommended)
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- [Docker](https://www.docker.com/) & Docker Compose


### 1. clone repo and get dependencies
```bash
git clone https://github.com/maximSytd/django-cash-flow.git
cd django-cash-flow
uv sync
```

### 2. activate virtual environment
```bash
# Windows:
.venv/Scripts/activate

# Unix/macOS:
source .venv/bin/activate
```


### 3. Create Django secrets in .env file
Create a `.env` file in the project directory with these variables:

```bash
DEBUG=true  # Set to false for production
DJANGO_SECRET="your-django-secret-key"
```

### 4.1 Database migrations
```bash
python manage.py migrate
```

### 4.2 Create admin user (optional)
```bash
python manage.py createsuperuser
```

### 5. Run the application
```bash
python manage.py runserver
```
Then open http://localhost:8000 in your browser