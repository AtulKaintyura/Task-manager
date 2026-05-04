import sqlite3

conn = sqlite3.connect("task_manager.db")
cursor = conn.cursor()

# users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT UNIQUE,
    password TEXT,
    role TEXT
)
""")

# projects table
cursor.execute("""
CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    created_by INTEGER,
    FOREIGN KEY (created_by) REFERENCES users(id)
)
""")

# tasks table
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    status TEXT,
    project_id INTEGER,
    assigned_to INTEGER,
    deadline TEXT,
    FOREIGN KEY (project_id) REFERENCES projects(id),
    FOREIGN KEY (assigned_to) REFERENCES users(id)
)
""")

conn.commit()
conn.close()

print("Database and tables created successfully")