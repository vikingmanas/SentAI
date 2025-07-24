from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/") 
db = client["sentimentDB"]
collection = db["reviews"]

def insert_review(text, sentiment, score):
    collection.insert_one({
        "text": text,
        "sentiment": sentiment,
        "score": score
    })

def get_sentiment_stats():
    pipeline = [
        {"$group": {"_id": "$sentiment", "count": {"$sum": 1}}}
    ]
    return list(collection.aggregate(pipeline))
