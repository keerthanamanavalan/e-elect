from flask import Flask, jsonify
import pandas as pd
import json
from flask_cors import CORS
import subprocess
app = Flask(__name__)
CORS(app)

@app.route('/get_columns', methods=['GET'])
def get_columns():
    try:
        # Read the Excel file
        df = pd.read_excel('D:/mini_proj/data/students_data.xlsx')

        # Convert NaN values to None
        df = df.where(pd.notnull(df), None)

        # Convert DataFrame to JSON string
        data_json = df.to_json(orient='split')

        # Convert JSON string to JSON object
        columns = json.loads(data_json)

        # Return the columns as JSON
        return jsonify(columns)
    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/run-python', methods=['GET'])
def run_python():
    # Run the Python file
    result = subprocess.run(['python3', 'script.py'], capture_output=True, text=True)
    return jsonify({'stdout': result.stdout, 'stderr': result.stderr})

if __name__ == '__main__':
    app.run(debug=True)
    app.run(port=5001)
