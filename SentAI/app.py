from flask import Flask, render_template, request
from textblob import TextBlob
from collections import Counter
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    if sentiment > 0:
        label = 'Positive'
    elif sentiment < 0:
        label = 'Negative'
    else:
        label = 'Neutral'

    with open('reviews/reviews.txt', 'a') as file:
        file.write(f'{label}: {text}\n')


    with open('reviews/reviews.txt', 'r') as file:
        lines = file.readlines()
    sentiments = [line.split(':')[0] for line in lines]
    sentiment_counts = Counter(sentiments)

    return render_template('result.html',
                           sentiment=label,
                           review=text,
                           sentiment_counts=sentiment_counts)

if __name__ == '__main__':
    os.makedirs('reviews', exist_ok=True)
    app.run(debug=True)
