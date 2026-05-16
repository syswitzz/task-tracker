<div align="center">

# Task Tracker API

Async task management REST API built with FastAPI and SQLAlchemy.

![Python](https://img.shields.io/badge/python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-async-green)
![License](https://img.shields.io/badge/license-MIT-orange)

</div>

---

## Features

- JWT Authentication
- OAuth2 Password Flow
- Async SQLAlchemy
- SQLite + aiosqlite
- User Management
- Task CRUD Operations
- User-specific Tasks
- Partial Updates with `PATCH`
- Task Completion Tracking

---

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/syswitzz/task-tracker-api.git
cd task-tracker-api
```

---

### 2. Install dependencies

This project uses `uv`.

```bash
uv sync
```

---

### 3. Configure environment variables

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

### 4. Run the development server

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

## Example Request

### Create Task

```bash
curl -X POST http://127.0.0.1:8000/tasks \
-H "Authorization: Bearer <token>" \
-H "Content-Type: application/json" \
-d '{"title":"Finish README","description":"Write project documentation"}'
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

<details>
<summary><strong>API Endpoints</strong></summary>

<br>

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

</details>

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

## Roadmap

- Task priority system
- Tags & categories
- Deadlines & reminders
- Stats & analytics
- Pagination & filtering
- Docker support
- Unit tests

---

## License

MIT