from extensions import db
from datetime import datetime

class Project(db.Model):
    __tablename__ = "projects"
     
    id =  db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(25), unique=True, nullable=False)
    desc = db.Column(db.String(50), nullable=False)
    status = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.timezone.utc)
    skill_id= db.Column(db.Integer, db.ForeignKey('skills.id'), nullable=False)
    
    def __repr__(self):
        return f"<Project {self.title}>"

