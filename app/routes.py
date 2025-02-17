from flask import Blueprint, jsonify

main = Blueprint('main', __name__, url_prefix='/api')

@main.route('/')
def home():
    return "Hello, Flask!"

# New API Endpoint
@main.route('/api/hello', methods=['GET'])
def api_hello():
    return jsonify({"message": "Hello from Flask API!"})

@main.route('/api/status', methods=['GET'])
def api_status():
    return jsonify({"status": "Running", "version": "1.0"})
=======
>>>>>>> bb80544 (first endpoint)
