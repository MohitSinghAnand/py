from extensions import db

class User:
    id = db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String(50), unique=True, Nullable=False)
    email = db.Column(db.String(254), unique=True, Nullable=False)
    
    def __repr__(self):
        return f"<User {self.username}>"