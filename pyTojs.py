from flask import Flask, jsonify
from flask_cors import CORS
import numpy as np
import matplotlib.pyplot as plt

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes
#x = [10,2,30]
#y = ["Henry","William","Richard"]

x2 = [2,22,33]
y2 = ['a','b','c']
# Create a plot using Matplotlib
"""plt.barh(y, x)
plt.title('Test Votes')
plt.savefig('simple_plot.png')"""
# Create a figure
fig = plt.figure(figsize=(10, 7))

# Plot the pie chart
plt.pie(x2, labels=y2)
# Save the plot as an image file (PNG format)
plt.savefig('simple_plot-1.png')
@app.route('/get_data')
def get_data():
    data = {'key': 'mfffg'}  # Your data to be sent
    return jsonify(1)

if __name__ == '__main__':
    app.run(debug=True)
