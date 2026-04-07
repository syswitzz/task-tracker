## Task Manager API

# WIP (work in progress)

# fix - cascade delete a user's post. currently it only deletes the user and not their post
# feat - add authentication (JWT). GET /me. POST /auth/register. POST /auth/login
# feat - add pagination and sorting. 
# feat - add priority (low, medium, high)
# refactor - dedicated action routes /task/{task_id}/complete or /task/{task_id}/uncomplete
# feat - tags/categories
POST /tags
GET /tags
POST /task/{task_id}/tags
GET /tasks?tag=work
# feat - deadlines/reminders
GET /tasks?due_today=true
GET /tasks?overdue=true
# feat - stats/analytics
GET /stats
GET /user/{user_id}/stats
# refactor - final structure
/auth
/users
/users/{id}
/users/{id}/tasks

/tasks
/tasks/{id}
/tasks/{id}/complete

/tags
/stats