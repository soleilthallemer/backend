from flask import Flask
from app.routes import api_blueprint
import os

app = Flask(__name__)
app.config.from_object("app.config.Config")

app.register_blueprint(api_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
