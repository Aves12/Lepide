
from flask import Flask, request, jsonify
from transformers import pipeline
import os

app = Flask(__name__)
summarizer = pipeline("summarization")

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    filepath = os.path.join("uploads", file.filename)
    file.save(filepath)
    return jsonify({"filepath": filepath})

@app.route('/summarize', methods=['POST'])
def summarize_file():
    data = request.get_json()
    filepath = data.get('filepath')
    if not filepath:
        return "Filepath is required", 400
    with open(filepath, 'r') as file:
        text = file.read()
    summary = summarizer(text, max_length=150, min_length=30, do_sample=False)
    return jsonify(summary[0])

if __name__ == '__main__':
    os.makedirs("uploads", exist_ok=True)
    app.run(debug=True)
