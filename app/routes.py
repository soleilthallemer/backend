from flask import Blueprint, jsonify

api_blueprint = Blueprint("api", __name__)

@api_blueprint.route("/api", methods=["GET"])
def api_home():
    return jsonify({"message": "Hello from Flask API!"})
