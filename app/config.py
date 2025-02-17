import os
from dotenv import load_dotenv
from urllib.parse import quote

# Load environment variables
load_dotenv(dotenv_path="/root/ArtemisAndSteamDir/backend/.env")

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret')

    # Load database credentials from environment variables
    MYSQL_USER = os.getenv("MYSQL_USER", "default_user")
    MYSQL_PASSWORD = quote(os.getenv("MYSQL_PASSWORD", "default_password"))  # <-- FIXED HERE
    MYSQL_DB = os.getenv("MYSQL_DB", "default_db")
    MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
    MYSQL_PORT = int(os.getenv("MYSQL_PORT", 3306))

    # Construct SQLAlchemy Database URI
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = os.getenv('FLASK_ENV', 'production') == 'development'
