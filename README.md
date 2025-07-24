# SENT AI - 🧠 AI-Based Sentiment Analyzer

[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-%23150458.svg?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-4.0-green?logo=mongodb)](https://www.mongodb.com/)
[![Hugging Face](https://img.shields.io/badge/HuggingFace-Transformers-yellow?logo=huggingface)](https://huggingface.co/transformers/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📌 Project Description

An **AI-Powered Sentiment Analyzer** that processes user-inputted reviews or text and classifies sentiment as **Positive**, **Negative**, or **Neutral** using transformer-based models. The results are visualized using dynamic charts in a user-friendly web interface.

---

## ⚙️ Tech Stack

- **Frontend:** HTML5, CSS3, JavaScript, Chart.js  
- **Backend:** Python, Flask  
- **AI/ML Model:** Hugging Face Transformers (`distilbert-base-uncased-finetuned-sst-2-english`)  
- **Database:** MongoDB  
- **APIs & Visualization:** Chart.js  
- **Deployment Ready:** Flask Localhost / Webserver

---

## 🚀 How to Run Locally

### 🔧 Prerequisites

- Python 3.10 or higher
- Node.js (for chart.js frontend assets if needed)
- MongoDB installed and running

### 📁 Folder Structure

```
SentAI/
│
├── static/
│   ├── style.css
│   └── chart.js
│
├── templates/
│   └── index.html
│
├── app.py
├── requirements.txt
└── README.md
```

---

### 🛠 Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourusername/SentAI.git
   cd SentAI
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start MongoDB service**

   Make sure your MongoDB is running locally on port 27017.

4. **Run the Flask app**
   ```bash
   python app.py
   ```

5. **Visit in browser**
   ```
   http://127.0.0.1:5000/
   ```

---

## 📈 Features

- 🔍 Real-time sentiment prediction using BERT
- 📊 Visual charts showing sentiment distribution
- 💾 MongoDB integration for storing past results
- ⚡ Fast and responsive UI with modern design

---

---

## 📄 License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for more info.

---

## 🤝 Contributing

Contributions are welcome!  
1. Fork this repo  
2. Create a new branch (`git checkout -b feature-branch`)  
3. Make changes and commit  
4. Push (`git push origin feature-branch`)  
5. Create a Pull Request

---

## 💡 Future Improvements

- Add multilingual sentiment support  
- Enhance UI/UX using React or Vue  
- Deploy on Render or Hugging Face Spaces

---

## 📬 Contact

Created with ❤️ by [Manas Dubey](https://github.com/vikingmanas)

