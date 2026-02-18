from extensions import db
from datetime import datetime

class Skill(db.Model):
    __tablename__ = "skills"
     
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    category = db.Column(db.String(15), nullable=False)
    progress = db.Column(db.Integer, nullable=False)
    projects = db.relationship('Project', backref='skill', lazy=True)
    created_at = db.Column(db.DateTime, default=datetime.timezone.utc)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    def __repr__(self):
        return f"<Skill {self.name}>"