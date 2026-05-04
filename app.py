import sqlite3
from flask import Flask, render_template,request,jsonify
app=Flask(__name__)

@app.route("/")
def signup_page():
    return render_template("signup.html")

@app.route("/login-page")
def login_page():
    return render_template("login.html")

@app.route("/dashboard-page")
def dashboard_page():
    return render_template("dashboard.html")
@app.route("/signup", methods=["POST"])
def signup():
    data = request.json

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    role = data.get("role")

    conn = sqlite3.connect("task_manager.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (name, email, password, role) VALUES (?, ?, ?, ?)",
        (name, email, password, role)
    )

    conn.commit()
    conn.close()

    return jsonify({
        "message": "User registered successfully"
    })

@app.route("/login", methods=["POST"])
def login():
    data = request.json

    email = data.get("email")
    password = data.get("password")

    conn = sqlite3.connect("task_manager.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email=? AND password=?",
        (email, password)
    )

    user = cursor.fetchone()
    conn.close()

    if user:
        return jsonify({
            "message": "Login successful",
            "user": {
                "id": user[0],
                "name": user[1],
                "email": user[2],
                "role": user[4]
            }
        })
    else:
        return jsonify({
            "message": "Invalid credentials"
        }), 401

@app.route("/projects", methods=["POST"])
def create_project():
    data = request.json

    name = data.get("name")
    created_by = data.get("created_by")

    conn = sqlite3.connect("task_manager.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO projects (name, created_by) VALUES (?, ?)",
        (name, created_by)
    )

    conn.commit()
    conn.close()

    return jsonify({
        "message": "Project created successfully"
    })

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.json

    title = data.get("title")
    status = data.get("status")
    project_id = data.get("project_id")
    assigned_to = data.get("assigned_to")
    deadline = data.get("deadline")

    conn = sqlite3.connect("task_manager.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO tasks (title, status, project_id, assigned_to, deadline)
        VALUES (?, ?, ?, ?, ?)
        """,
        (title, status, project_id, assigned_to, deadline)
    )

    conn.commit()
    conn.close()

    return jsonify({
        "message": "Task created and assigned successfully"
    })

@app.route("/tasks", methods=["GET"])
def get_tasks():
    conn = sqlite3.connect("task_manager.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    conn.close()

    task_list = []

    for task in tasks:
        task_list.append({
            "id": task[0],
            "title": task[1],
            "status": task[2],
            "project_id": task[3],
            "assigned_to": task[4],
            "deadline": task[5]
        })

    return jsonify({
        "tasks": task_list
    })

@app.route("/tasks/<int:id>", methods=["PUT"])
def update_task(id):
    data = request.json
    new_status = data.get("status")

    conn = sqlite3.connect("task_manager.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE tasks SET status=? WHERE id=?",
        (new_status, id)
    )

    conn.commit()
    conn.close()

    return jsonify({
        "message": "Task status updated"
    })

@app.route("/dashboard", methods=["GET"])
def dashboard():
    conn = sqlite3.connect("task_manager.db")
    cursor = conn.cursor()

    # total tasks
    cursor.execute("SELECT COUNT(*) FROM tasks")
    total_tasks = cursor.fetchone()[0]

    # completed tasks
    cursor.execute("SELECT COUNT(*) FROM tasks WHERE status='completed'")
    completed_tasks = cursor.fetchone()[0]

    # pending tasks
    cursor.execute("SELECT COUNT(*) FROM tasks WHERE status='pending'")
    pending_tasks = cursor.fetchone()[0]

    conn.close()

    return jsonify({
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "pending_tasks": pending_tasks
    })

if __name__ == "__main__":
    app.run(debug=True)