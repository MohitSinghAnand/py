from flask import Flask
from flask_cors import CORS
from routes.api import api   
from extensions import db
import models

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)
db.init_app(app)

app.register_blueprint(api, url_prefix="/api")

@app.route("/")
def root():
    return {"message": "Server is running"}


if __name__ == "__main__":
    with app.app_context(): 
        
        db.create_all()
        print("tables created")
    app.run(debug=True)



    