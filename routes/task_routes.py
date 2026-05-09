from flask import Blueprint, request, jsonify
from database.db import db
from models.task import Task
from flask_socketio import emit

task_bp = Blueprint("task_bp", __name__, url_prefix="/api/tasks")


@task_bp.route("", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()

    task_list = []

    for task in tasks:
        task_list.append({
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "priority": task.priority,
            "status": task.status,
            "created_date": task.created_date.strftime("%Y-%m-%d %H:%M:%S")
        })

    return jsonify(task_list), 200


@task_bp.route("", methods=["POST"])
def add_task():
    data = request.get_json()

    new_task = Task(
        title=data.get("title"),
        description=data.get("description"),
        priority=data.get("priority"),
        status=data.get("status")
    )

    db.session.add(new_task)
    db.session.commit()

    emit("task_update", {"message": "New task added successfully"}, broadcast=True, namespace="/")

    return jsonify({"message": "Task added successfully"}), 201


@task_bp.route("/<int:id>", methods=["PUT"])
def update_task(id):
    task = Task.query.get_or_404(id)

    data = request.get_json()

    task.title = data.get("title", task.title)
    task.description = data.get("description", task.description)
    task.priority = data.get("priority", task.priority)
    task.status = data.get("status", task.status)

    db.session.commit()

    emit("task_update", {"message": "Task updated successfully"}, broadcast=True, namespace="/")

    return jsonify({"message": "Task updated successfully"}), 200


@task_bp.route("/<int:id>", methods=["DELETE"])
def delete_task(id):
    task = Task.query.get_or_404(id)

    db.session.delete(task)
    db.session.commit()

    emit("task_update", {"message": "Task deleted successfully"}, broadcast=True, namespace="/")

    return jsonify({"message": "Task deleted successfully"}), 200