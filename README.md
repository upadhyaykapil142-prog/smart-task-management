# Smart Task Management System

A Flask-based Smart Task Management System with REST APIs, Analytics, and Real-Time Notifications using WebSockets.

---

## Features

- User Authentication
- Add Tasks
- Update Tasks
- Delete Tasks
- Task Analytics
- Completion Percentage
- Real-Time Notifications using Flask-SocketIO
- Responsive Dashboard UI
- PostgreSQL/SQLite Database Integration

---

## Tech Stack

- Python
- Flask
- Flask-SocketIO
- SQLAlchemy
- Pandas
- NumPy
- HTML
- CSS
- JavaScript

---

## Project Structure

smart-task-management/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
│
├── database/
│ └── db.py
│
├── models/
│ ├── task.py
│ └── user.py
│
├── routes/
│ ├── auth_routes.py
│ ├── analytics_routes.py
│ └── task_routes.py
│
├── static/
│ ├── style.css
│ └── script.js
│
└── templates/
├── dashboard.html
├── login.html
└── register.html

---

## Installation

### Clone Repository

```bash
git clone <your-github-link>
cd smart-task-management
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Project

```bash
python app.py
```

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/tasks | Get All Tasks |
| POST | /api/tasks | Add New Task |
| PUT | /api/tasks/<id> | Update Task |
| DELETE | /api/tasks/<id> | Delete Task |

---

## Future Improvements

- JWT Authentication
- Email Notifications
- Task Categories
- Deadline Reminder System
- Deployment on Render/Heroku

---

## Author

Kapil Upadhyay