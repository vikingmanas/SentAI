from flask import Flask, render_template, request, jsonify
from utils.sentiment_analyzer import analyze_sentiment
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client.sentimentDB
collection = db.reviews

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data['text']
    result = analyze_sentiment(text)
    collection.insert_one({"text": text, "result": result})
    return jsonify(result)

@app.route('/chart-data')
def chart_data():
    counts = {"POSITIVE": 0, "NEGATIVE": 0, "NEUTRAL": 0}
    for doc in collection.find():
        label = doc["result"]["label"]
        if label in counts:
            counts[label] += 1
    return jsonify(counts)

if __name__ == '__main__':
    app.run(debug=True)
