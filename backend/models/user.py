from extensions import db
from datetime import datetime

class User(db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(254), unique=True, nullable=False)
    hash = db.Column(db.String(60), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.timezone.utc)
    skills = db.relationship('Skill', backref='user', lazy=True)
    
    def __repr__(self):
        return f"<User {self.username}>"