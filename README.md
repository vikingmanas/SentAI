# 💬 SentAI - AI-Based Sentiment Analyzer

Analyze user sentiment from social media posts, product reviews, or any free-form text using powerful Transformer-based models.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-green.svg)
![Hugging Face](https://img.shields.io/badge/Hugging--Face-Transformers-yellow.svg)
![MongoDB](https://img.shields.io/badge/MongoDB-Database-brightgreen.svg)

---

## 📌 Features

- 🔍 Analyze sentiment (Positive / Negative / Neutral)
- 📊 Visual representation using Chart.js
- 🧠 Powered by Hugging Face Transformers
- 💾 Store analysis results in MongoDB
- 🌐 Simple and interactive web UI (Flask + Bootstrap)

---

## 📂 Project Structure

```
SentAI/
├── app.py
├── static/
│   └── chart.js
├── templates/
│   ├── index.html
│   └── result.html
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/SentAI.git
cd SentAI
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the App

```bash
python app.py
```

Then, open your browser and navigate to:

```
http://127.0.0.1:5000
```

---

## 🧠 Model Used

Using Hugging Face's `distilbert-base-uncased-finetuned-sst-2-english` model for sentiment analysis.

```python
from transformers import pipeline
sentiment_pipeline = pipeline("sentiment-analysis")
```

---

## 🖼️ Demo

![Demo Screenshot](assets/demo.gif) <!-- Replace with actual GIF or image path -->

---

## 📦 Requirements

- Python 3.10+
- Flask
- transformers
- torch
- MongoDB (local or Atlas)

Install via:

```bash
pip install flask transformers torch pymongo
```

---

## 📌 Sample Input

> "This product exceeded all my expectations!"

## ✅ Sample Output

```json
{
  "label": "POSITIVE",
  "score": 0.9992
}
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

---

## 📄 License

MIT License © [Your Name](https://github.com/yourusername)

---

## 🙋‍♂️ Author

- **Manas Dubey**  
  💼 [LinkedIn](https://www.linkedin.com/in/your-profile)  
  💻 [GitHub](https://github.com/vikingmanas)

---

## 🌟 Don't forget to star this repo if you found it useful!
