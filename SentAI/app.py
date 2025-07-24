from flask import Flask, request, render_template, jsonify
from sentiment_model import analyze_sentiment
from db import insert_review, get_sentiment_stats

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['review']
    result = analyze_sentiment(text)
    insert_review(text, result['label'], result['score'])
    return jsonify(result)

@app.route('/stats', methods=['GET'])
def stats():
    data = get_sentiment_stats()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
