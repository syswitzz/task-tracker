<div align="center">

# 🚀 Task Tracker API

**A modern asynchronous task management REST API built with FastAPI, SQLAlchemy, and JWT Authentication.**

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge\&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Async-009688?style=for-the-badge\&logo=fastapi)
![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?style=for-the-badge\&logo=sqlite)
![License](https://img.shields.io/badge/License-MIT-orange?style=for-the-badge)

<br>

Secure user authentication, task management, and user-specific task tracking with a fully asynchronous backend architecture.

[Features](#-features) • [Quick Start](#-quick-start) • [API Docs](#-api-documentation) • [Endpoints](#-api-endpoints) • [Roadmap](#-roadmap)

</div>

---

## ✨ Features

### 🔐 Authentication & Security

* JWT Authentication
* OAuth2 Password Flow
* Protected endpoints
* User-specific data access

### 📋 Task Management

* Create, read, update, and delete tasks
* Partial updates using `PATCH`
* Task completion tracking
* User-owned task isolation

### ⚡ Modern Backend Stack

* Fully asynchronous architecture
* FastAPI framework
* Async SQLAlchemy ORM
* SQLite with `aiosqlite`

---

## 🛠️ Tech Stack

| Layer           | Technology         |
| --------------- | ------------------ |
| Framework       | FastAPI            |
| Language        | Python 3.12        |
| ORM             | SQLAlchemy (Async) |
| Database        | SQLite             |
| Authentication  | JWT + OAuth2       |
| ASGI Server     | Uvicorn            |
| Package Manager | uv                 |

---

## 🚀 Quick Start

### Clone Repository

```bash
git clone https://github.com/syswitzz/task-tracker-api.git
cd task-tracker-api
```

### Install Dependencies

```bash
uv sync
```

### Configure Environment Variables

Create a `.env` file:

```env
SECRET_KEY=your_secret_key
ACCESS_TOKEN_EXPIRE_MINUTES=30
ALGORITHM=HS256
```

Generate a secure key:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

### Run Development Server

```bash
uv run uvicorn main:app --reload
```

Server will start at:

```text
http://127.0.0.1:8000
```

---

## 📚 API Documentation

| Interface  | URL                           |
| ---------- | ----------------------------- |
| Swagger UI | `http://127.0.0.1:8000/docs`  |
| ReDoc      | `http://127.0.0.1:8000/redoc` |

> Swagger UI includes built-in JWT authentication via the **Authorize** button.

---

## 🗄️ Database

SQLite is used as the default database.

```text
tasks.db
```

The database is automatically initialized when the application starts.

---

## 🔗 API Endpoints

<details>
<summary><strong>👤 User Endpoints</strong></summary>

| Method | Endpoint           | Description                 |
| ------ | ------------------ | --------------------------- |
| POST   | `/users`           | Register user               |
| GET    | `/users`           | Get all users               |
| POST   | `/users/token`     | Login & obtain access token |
| GET    | `/users/me`        | Current authenticated user  |
| PUT    | `/users/{user_id}` | Update user                 |
| DELETE | `/users/{user_id}` | Delete user                 |

</details>

<details>
<summary><strong>📝 Task Endpoints</strong></summary>

| Method | Endpoint                      | Description              |
| ------ | ----------------------------- | ------------------------ |
| GET    | `/tasks`                      | Get all tasks            |
| POST   | `/tasks`                      | Create task              |
| GET    | `/tasks/me`                   | Get current user's tasks |
| GET    | `/tasks/{task_id}`            | Get task by ID           |
| PATCH  | `/tasks/{task_id}`            | Update task              |
| DELETE | `/tasks/{task_id}`            | Delete task              |
| POST   | `/tasks/{task_id}/complete`   | Mark completed           |
| POST   | `/tasks/{task_id}/incomplete` | Mark incomplete          |

</details>

---

## 🧪 Example Request

### Create a Task

```bash
curl -X POST http://127.0.0.1:8000/tasks \
-H "Authorization: Bearer <token>" \
-H "Content-Type: application/json" \
-d '{
  "title":"Finish README",
  "description":"Write project documentation"
}'
```

### Response

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

## 📁 Project Structure

```text
task-tracker-api/
├── router/
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

## 🗺️ Roadmap

* [x] JWT Authentication
* [x] Async SQLAlchemy
* [x] User-specific Tasks
* [x] Task Completion Tracking
* [ ] Task Priorities
* [ ] Tags & Categories
* [ ] Deadlines & Reminders
* [ ] Pagination & Filtering
* [ ] Docker Support
* [ ] Unit Tests
* [ ] PostgreSQL Support

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

---

## 📄 License

Licensed under the MIT License.

---

<div align="center">

Built with ❤️ using FastAPI & Python

</div>
