# Task Tracker API

A simple async REST API for task management built with FastAPI.

Features include JWT authentication, user management, task CRUD operations, and task completion tracking.

---

## Tech Stack

- Python 3.12+
- FastAPI
- SQLAlchemy
- SQLite + aiosqlite
- JWT Authentication
- Pydantic Settings
- uv

---

## Setup

### Clone the repository

```bash
git clone https://github.com/syswitzz/task-tracker-api.git
cd task-tracker-api
```

### Install dependencies

```bash
uv sync
```

---

## Environment Variables

Create a `.env` file in the root directory.

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

## Run the server

```bash
uv run uvicorn main:app --reload
```

Server runs at:

```text
http://127.0.0.1:8000
```

---

## API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

The Swagger Authorize button supports JWT authentication using OAuth2 password flow.

---

## Database

The project uses SQLite with `aiosqlite`.

Database file:

```text
tasks.db
```

The database is automatically created on startup.

---

## Features

### Authentication

- JWT authentication
- OAuth2 password flow
- Protected routes with Bearer token

### Users

- Create users
- Get all users
- Get current authenticated user
- Update users
- Delete users

### Tasks

- Create tasks
- Get all tasks
- Get tasks for current user
- Update tasks partially using PATCH
- Delete tasks
- Mark tasks complete/incomplete

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
├── README.md
└── .gitignore
```

---

## Roadmap

### Priority System

- Low / medium / high task priority

### Tags & Categories

Possible endpoints:

```text
POST /tags
GET /tags
POST /task/{task_id}/tags
GET /tasks?tag=work
```

### Deadlines & Reminders

Possible filters:

```text
GET /tasks?due_today=true
GET /tasks?overdue=true
```

### Stats & Analytics

Possible endpoints:

```text
GET /stats
GET /user/{user_id}/stats
```

---

## License

MIT