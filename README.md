# Task Tracker API

Async task management REST API built with FastAPI.

Supports JWT authentication, user management, task CRUD operations, and task completion tracking.

---

## Tech Stack

- Python 3.12+
- FastAPI
- SQLAlchemy
- SQLite + aiosqlite
- Pydantic Settings
- JWT Authentication
- uv

---

## Features

### Authentication

- JWT authentication
- OAuth2 password flow
- Bearer token protected routes

### Users

- Create users
- Get all users
- Get current authenticated user
- Update users
- Delete users

### Tasks

- Create tasks
- Get all tasks
- Get current user's tasks
- Partially update tasks using `PATCH`
- Delete tasks
- Mark tasks complete/incomplete

---

# Setup

## 1. Clone the repository

```bash
git clone https://github.com/syswitzz/task-tracker-api.git
cd task-tracker-api
```

---

## 2. Install dependencies

This project uses `uv`.

Install dependencies:

```bash
uv sync
```

---

## 3. Create environment variables

Create a `.env` file in the project root.

```env
SECRET_KEY=your_secret_key
ACCESS_TOKEN_EXPIRE_MINUTES=30
ALGORITHM=HS256
```

Generate a secure secret key:

```bash
python3 -c "import secrets; print(secrets.token_hex(32))"
```

---

## 4. Run the server

```bash
uv run uvicorn main:app --reload
```

Server starts at:

```text
http://127.0.0.1:8000
```

---

## API Documentation

| Service | URL |
|---|---|
| Swagger UI | `http://127.0.0.1:8000/docs` |
| ReDoc | `http://127.0.0.1:8000/redoc` |

Swagger UI supports JWT authentication using the built-in **Authorize** button.

---

## Database

The project uses SQLite with `aiosqlite`.

Database file:

```text
tasks.db
```

The database is automatically created on startup.

---

## API Endpoints

### Users

| Method | Endpoint | Description |
|---|---|---|
| GET | `/users` | Get all users |
| POST | `/users` | Create user |
| POST | `/users/token` | Login and get access token |
| GET | `/users/me` | Get current authenticated user |
| PUT | `/users/{user_id}` | Update user |
| DELETE | `/users/{user_id}` | Delete user |

---

### Tasks

| Method | Endpoint | Description |
|---|---|---|
| GET | `/tasks` | Get all tasks |
| POST | `/tasks` | Create task |
| GET | `/tasks/me` | Get current user's tasks |
| GET | `/tasks/{task_id}` | Get task by ID |
| PATCH | `/tasks/{task_id}` | Partially update task |
| DELETE | `/tasks/{task_id}` | Delete task |
| POST | `/tasks/{task_id}/complete` | Mark task completed |
| POST | `/tasks/{task_id}/incomplete` | Mark task incomplete |

---

## Example Request

### Create Task

```http
POST /tasks
```

Request body:

```json
{
  "title": "Finish README",
  "description": "Write project documentation"
}
```

Example response:

```json
{
  "id": 1,
  "title": "Finish README",
  "description": "Write project documentation",
  "completed": false,
  "user_id": 1
}
```

---

## Project Structure

```text
.
├── router/
│   ├── __init__.py
│   ├── tasks.py
│   └── users.py
├── auth.py
├── config.py
├── database.py
├── main.py
├── models.py
├── schemas.py
├── pyproject.toml
├── uv.lock
└── README.md
```

---

## Roadmap/ TODO

Feel free to contribute

- Task priority system
- Tags & categories
- Deadlines & reminders
- Stats & analytics
- Pagination & filtering
- Docker support
- Unit tests

---