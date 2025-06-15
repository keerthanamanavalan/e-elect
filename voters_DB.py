from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import os
app = Flask(__name__)
CORS(app)
if not os.path.isfile('database.db'):
    
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS values_table (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                column1 TEXT NOT NULL,
                column2 TEXT NOT NULL,
                column3 NUMBER NOT NULL
            )
        ''')

        conn.commit()
        conn.close()
        print("Database initialization successful")

@app.route('/store-values', methods=['POST'])
def store_values():
    data = request.json
    column1 = data.get('column1')
    column2 = data.get('column2')
    column3 = data.get('column3')

    if column1 and column2 and column3:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO values_table (column1, column2, column3) VALUES (?, ?, ?)', (column1, column2, column3))
        conn.commit()
        conn.close()
        print(f"Stored values: column1={column1}, column2={column2}, column3={column3}")  # Debugging information
        return jsonify({"message": "Values stored successfully"}), 201
    else:
        return jsonify({"message": "Missing values"}), 400

@app.route('/check-values', methods=['POST'])
def check_values():
    data = request.json
    column1 = data.get('column1')
    column2 = data.get('column2')
    column3 = data.get('column3')

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM values_table WHERE column1 = ? AND column2 = ? AND column3 = ?', (column1, column2, column3))
    result = cursor.fetchone()
    conn.close()

    if result:
        return jsonify({"exists": True})
    else:
        return jsonify({"exists": False})

@app.route('/list-values', methods=['GET'])
def list_values():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM values_table')
    results = cursor.fetchall()
    conn.close()

    return jsonify(results)

if __name__ == '__main__':
   # init_db()
    app.run(debug=True)
    app.run(port=5500)
