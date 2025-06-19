import psycopg2
from dotenv import load_dotenv
import os
from pathlib import Path

# Load .env from the ROOT directory (one level up from backend/)
dotenv_path = Path(__file__).resolve().parents[1] / '.env'
load_dotenv(dotenv_path)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )
    return conn
