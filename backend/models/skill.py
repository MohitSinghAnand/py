from extensions import db

class User:
    id = db.Column(db.Integer, primary_Key=True)
    name = db.Column(db.String(25), Nullable=False)
    category = db.Column(db.String(15), Nullable=False)
    progress = db.Column(db.Integer, Nullable=False)
    user_id = db.Column(primary)