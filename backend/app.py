from flask import Flask, jsonify
from flask_cors import CORS
from db import get_db_connection  # ✅ DB connection logic moved to db.py

app = Flask(__name__)
CORS(app)  # ✅ Enables cross-origin requests (needed for frontend)

@app.route('/')
def home():
    return jsonify({"message": "Flask backend is running!"})

@app.route('/criminals')
def get_criminals():
    conn = get_db_connection()  # ✅ Centralized connection handling
    if not conn:
        return jsonify({"error": "Database connection failed"}), 500

    cur = conn.cursor()
    cur.execute("SELECT * FROM criminals;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    return jsonify(rows)

if __name__ == '__main__':
    print("App is starting...")
    app.run(debug=True)
