import os
import time
import psycopg2
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# This allows our frontend website to safely talk to this backend server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Fetch the database connection string from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

def get_db_connection():
    """Retries connection to the database if it isn't ready immediately."""
    retries = 5
    while retries > 0:
        try:
            conn = psycopg2.connect(DATABASE_URL)
            return conn
        except psycopg2.OperationalError:
            retries -= 1
            print("Database initializing... waiting 2 seconds.")
            time.sleep(2)
    raise Exception("Could not connect to the database.")

# Initialize the database table when the backend starts up
conn = get_db_connection()
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id SERIAL PRIMARY KEY,
        title TEXT NOT NULL
    );
""")
conn.commit()
cursor.close()
conn.close()

class Task(BaseModel):
    title: str

@app.get("/tasks", response_model=List[str])
def get_tasks():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT title FROM tasks;")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    # Flatten the list of tuples returned by Postgres: [('Task 1',), ('Task 2',)] -> ['Task 1', 'Task 2']
    return [row[0] for row in rows]

@app.post("/tasks")
def add_task(task: Task):
    if task.title.strip():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tasks (title) VALUES (%s);", (task.title,))
        conn.commit()
        cursor.close()
        conn.close()
        return {"message": "Task saved to database!"}
    return {"error": "Task cannot be empty"}