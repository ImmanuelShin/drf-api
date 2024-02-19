# Lab - Class 31

## Project: DRF and Docker

### Author: [Immanuel Shin](https://github.com/ImmanuelShin)

A small web application showcasing DRF and Docker.

### Setup

#### Requirements

- Docker: Ensure that you have Docker installed on your machine.

**How to initialize/run your application:**

  1. Clone the repository.
   ```bash
   git clone
   ```
  2. Navigate to the project directory.
   ```bash
   cd [name-of-directory]
   ```
  3. Activate your virtual environment (if applicable).
   ```bash
   `python3 -m venv .venv`

   `source .venv/bin/activate` (Linux/Mac)

   `source .venv/Scripts/activate` (Windows)
   ```
  4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
  5. Apply migrations:
  ```bash
  python manage.py migrate
  ```
  6. **Optional** Create a superuser (admin account) for Django admin access:
  ```bash
  python manage.py createsuperuser
  ```
  Follow the prompts to set up your admin account.
  7. Build and run the Docker containers:
  ```bash
  docker-compose up --build
  ```
  8. The application will be accessible at http://localhost:8000/ or http://127.0.0.1:8000/.  
    - API access at /api/v1/drfs endpoint (e.g http://127.0.0.1:8000/api/v1/drfs/)
      - Individual details access at /[index] endpoint (e.g http://127.0.0.1:8000/api/v1/drfs/1/)