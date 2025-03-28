# prompt-library

## Introduction
This project is a FastAPI-based application that provides API endpoints for managing categories, subcategories, and prompts. The application is containerized using Docker and can be deployed locally for testing and development.

---

## Prerequisites
- Python 3.8+
- Docker
- Git

### Install Dependencies
```bash
pip install -r requirements.txt
```

## Running Locally

### Clone the Repository
```bash
git clone https://github.com/username/your-repo.git
cd your-repo
```

### Run Using Docker
#### Build the Docker Image
```bash
docker build -t fastapi-app .
```

#### Run the Docker Container
```bash
docker run -d -p 8000:8000 fastapi-app
```

### Access the Application
Visit the API docs at:
```
http://localhost:8000/docs
```

### Run Without Docker
#### Start the Application
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Environment Variables
Create a `.env` file to configure environment-specific settings.

---

## Project Structure
```
your_project/
├── app/
│   ├── api/
│   │   └── endpoints/
│   │       ├── categories.py
│   │       ├── subcategories.py
│   │       └── prompts.py
│   └── main.py
├── Dockerfile
├── requirements.txt
└── README.md
```

## API Endpoints
- `/` - Root endpoint to check server status
- `/categories` - Manage categories
- `/subcategories` - Manage subcategories
- `/prompts` - Manage prompts

## Troubleshooting
If you encounter issues, check the Docker logs:
```bash
docker logs fastapi-app
```

For further assistance, contact the maintainer.

