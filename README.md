# Test task:
Implement django app that will implement the tree menu

## 🚀 Project Setup Guide (local)

This guide will help you set up and run the Django project using the [uv](https://docs.astral.sh/uv/getting-started/installation/) Python package manager.

### ✅ Prerequisites

- [Python](https://www.python.org/) (3.11+ recommended)
- [uv](https://docs.astral.sh/uv/getting-started/installation/)


### 1. clone repo and get dependencies
```bash
git clone https://github.com/maximSytd/django-menu-tree.git
cd django-menu-tree
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