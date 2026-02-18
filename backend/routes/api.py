
from flask import Blueprint, jsonify

api = Blueprint("api", __name__)

@api.route("/")
def home():
    return jsonify({"message": "Running"})

@api.route("/test")
def test():
    return jsonify({"status": "working"})
