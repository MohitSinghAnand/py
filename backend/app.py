from flask import Flask
from flask_cors import CORS
from routes.api import api
from extensions import db

app = Flask(__name__)
db .init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)

app.register_blueprint(api, url_prefix="/api")

if __name__ == "__main__":
    with app.app_context(): 
        db.create_all()
    app.run(debug=True)



    