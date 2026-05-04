# Team Task Manager (Full Stack Project)

A full-stack task management web application built using Flask, SQLite, HTML, CSS, and JavaScript.

This project allows teams to create projects, assign tasks to members, update task progress, and track overall task statistics through a dashboard.

---

## Features

### Authentication
- User Signup
- User Login
- Role selection (Admin / Member)

### Project Management
- Create new projects
- Store project details in database

### Task Management
- Create tasks
- Assign tasks to team members
- Set task deadlines
- Update task status (Pending / Completed)
- View all tasks

### Dashboard
- Total tasks count
- Completed tasks count
- Pending tasks count

---

## Tech Stack

### Backend
- Python
- Flask
- SQLite

### Frontend
- HTML
- CSS
- JavaScript
- Fetch API

### Tools
- Postman
- Git/GitHub
- Railway (for deployment)

---

## Project Structure

```bash
project-folder/
│
├── app.py
├── task_manager.db
│
├── templates/
│   ├── signup.html
│   ├── login.html
│   └── dashboard.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── README.md
