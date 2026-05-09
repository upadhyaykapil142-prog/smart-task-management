from database.db import db
from datetime import datetime

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(200), nullable=False)

    description = db.Column(db.Text, nullable=False)

    priority = db.Column(db.String(50), nullable=False)

    status = db.Column(db.String(50), default="Pending")

    created_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Task {self.title}>"