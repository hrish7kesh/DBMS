from flask import Flask, jsonify, request
from flask_cors import CORS
from db import get_db_connection

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({'message': 'Flask backend is running!'})

@app.route('/criminals', methods=['GET'])
def get_criminals():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM criminals')
    criminals = cur.fetchall()
    columns = [desc[0] for desc in cur.description]
    result = [dict(zip(columns, row)) for row in criminals]
    cur.close()
    conn.close()
    return jsonify(result)

# Add a new criminal
@app.route('/criminals', methods=['POST'])
def add_criminal():
    data = request.get_json()
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO criminals (first_name, last_name, date_of_birth, gender, address, national_id, is_wanted)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    ''', (
        data['first_name'],
        data['last_name'],
        data['date_of_birth'],
        data['gender'],
        data['address'],
        data['national_id'],
        data['is_wanted']
    ))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Criminal added successfully'}), 201

# UPDATE a criminal
@app.route('/criminals/<int:criminal_id>', methods=['PUT'])
def update_criminal(criminal_id):
    data = request.get_json()
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE criminals
        SET first_name = %s,
            last_name = %s,
            date_of_birth = %s,
            gender = %s,
            address = %s,
            national_id = %s,
            is_wanted = %s
        WHERE criminal_id = %s
        """, (
            data['first_name'],
            data['last_name'],
            data['date_of_birth'],
            data['gender'],
            data['address'],
            data['national_id'],
            data['is_wanted'],
            criminal_id
        )
    )
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Criminal updated successfully'}), 200


# DELETE a criminal
@app.route('/criminals/<int:criminal_id>', methods=['DELETE'])
def delete_criminal(criminal_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM criminals WHERE criminal_id = %s', (criminal_id,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Criminal deleted successfully'}), 200

@app.route('/crimes', methods=['GET'])
def get_crimes():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM crimes')
    crimes = cur.fetchall()
    columns = [desc[0] for desc in cur.description]
    result = [dict(zip(columns, row)) for row in crimes]
    cur.close()
    conn.close()
    return jsonify(result)

@app.route('/crimes', methods=['POST'])
def add_crime():
    data = request.get_json()
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO crimes (crime_type, description, location, crime_date)
        VALUES (%s, %s, %s, %s)
    ''', (data['crime_type'], data['description'], data['location'], data['crime_date']))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Crime added successfully'}), 201

@app.route('/crimes/<int:crime_id>', methods=['PUT'])
def update_crime(crime_id):
    data = request.get_json()
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        UPDATE crimes
        SET crime_type = %s, description = %s, location = %s, crime_date = %s
        WHERE crime_id = %s
    ''', (data['crime_type'], data['description'], data['location'], data['crime_date'], crime_id))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Crime updated successfully'}), 200

@app.route('/crimes/<int:crime_id>', methods=['DELETE'])
def delete_crime(crime_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM crimes WHERE crime_id = %s', (crime_id,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Crime deleted successfully'}), 200

@app.route('/officers', methods=['GET'])
def get_officers():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM officers')
    officers = cur.fetchall()
    columns = [desc[0] for desc in cur.description]
    result = [dict(zip(columns, row)) for row in officers]
    cur.close()
    conn.close()
    return jsonify(result)

@app.route('/officers', methods=['POST'])
def add_officer():
    data = request.get_json()
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO officers (name, rank, station, email, phone)
        VALUES (%s, %s, %s, %s, %s)
    ''', (data['name'], data['rank'], data['station'], data['email'], data['phone']))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Officer added successfully'}), 201

@app.route('/officers/<int:officer_id>', methods=['PUT'])
def update_officer(officer_id):
    data = request.get_json()
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        UPDATE officers
        SET name = %s, rank = %s, station = %s, email = %s, phone = %s
        WHERE officer_id = %s
    ''', (data['name'], data['rank'], data['station'], data['email'], data['phone'], officer_id))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Officer updated successfully'}), 200

@app.route('/officers/<int:officer_id>', methods=['DELETE'])
def delete_officer(officer_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM officers WHERE officer_id = %s', (officer_id,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Officer deleted successfully'}), 200

@app.route('/cases', methods=['GET'])
def get_cases():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM cases')
    cases = cur.fetchall()
    columns = [desc[0] for desc in cur.description]
    result = [dict(zip(columns, row)) for row in cases]
    cur.close()
    conn.close()
    return jsonify(result)

@app.route('/cases', methods=['POST'])
def add_case():
    data = request.get_json()
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO cases (officer_id, crime_id, status, assigned_date, remarks)
        VALUES (%s, %s, %s, %s, %s)
    ''', (data['officer_id'], data['crime_id'], data['status'], data['assigned_date'], data['remarks']))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Case added successfully'}), 201

@app.route('/cases/<int:case_id>', methods=['PUT'])
def update_case(case_id):
    data = request.get_json()
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        UPDATE cases
        SET officer_id = %s, crime_id = %s, status = %s, assigned_date = %s, remarks = %s
        WHERE case_id = %s
    ''', (data['officer_id'], data['crime_id'], data['status'], data['assigned_date'], data['remarks'], case_id))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Case updated successfully'}), 200

@app.route('/cases/<int:case_id>', methods=['DELETE'])
def delete_case(case_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM cases WHERE case_id = %s', (case_id,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Case deleted successfully'}), 200

if __name__ == '__main__':
    print("App is starting...")
    app.run(debug=True)
