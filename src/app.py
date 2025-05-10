from flask import Flask, render_template, jsonify, send_from_directory
import json
from pathlib import Path

app = Flask(__name__)

def load_analysis_data(filename='emote_analysis.json'):
    """Load analysis data from a JSON file."""
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            print("Loaded data:", data)  # Debug print
            return data
    except FileNotFoundError:
        print(f"File {filename} not found")  # Debug print
        return None
    except Exception as e:
        print(f"Error loading analysis data: {str(e)}")  # Debug print
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data')
def get_data():
    data = load_analysis_data()
    if data is None:
        return jsonify({'error': 'No data available'}), 404
    return jsonify(data)

@app.route('/monthly.html')
def monthly_html():
    return render_template('monthly.html')

@app.route('/monthly')
def monthly():
    return render_template('monthly.html')

@app.route('/emote_monthly_usage.csv')
def serve_monthly_csv():
    return send_from_directory('.', 'emote_monthly_usage.csv')

if __name__ == '__main__':
    app.run(debug=True) 