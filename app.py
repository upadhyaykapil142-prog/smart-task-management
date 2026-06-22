from flask import Flask, render_template
from flask_socketio import SocketIO
from config import Config
from database.db import db
from routes.task_routes import task_bp
from models.task import Task

import pandas as pd
import numpy as np

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

socketio = SocketIO(app)

app.register_blueprint(task_bp)


@app.route("/")
def home():
    return "Smart Task Management System Running Successfully"


@app.route("/dashboard")
def dashboard():

    tasks = Task.query.all()

    # Convert tasks into dataframe
    task_data = []

    for task in tasks:
        task_data.append({
            "title": task.title,
            "status": task.status
        })

    df = pd.DataFrame(task_data)

    total_tasks = len(df)

    completed_tasks = len(df[df["status"] == "Completed"]) if not df.empty else 0

    pending_tasks = len(df[df["status"] == "Pending"]) if not df.empty else 0

    completion_percentage = (
        np.round((completed_tasks / total_tasks) * 100, 2)
        if total_tasks > 0 else 0
    )

    return render_template(
        "dashboard.html",
        tasks=tasks,
        total_tasks=total_tasks,
        completed_tasks=completed_tasks,
        pending_tasks=pending_tasks,
        completion_percentage=completion_percentage
    )


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    socketio.run(app, host="0.0.0.0", port=10000)