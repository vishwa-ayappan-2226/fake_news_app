from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Simple demo prediction logic (replace with real ML later)
def predict_fake_news(text):
    fake_words = ["clickbait", "shocking", "unbelievable", "fake", "scam"]
    return 0 if any(word in text.lower() for word in fake_words) else 1

@app.route("/", methods=["GET"])
def home():
    return "Fake News Detection API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    text = data.get("news", "")

    if text.strip() == "":
        return jsonify({"result": "Please enter some news text"}), 400

    pred = predict_fake_news(text)
    result = "Fake" if pred == 0 else "Real"

    return jsonify({"result": result})

if __name__ == "__main__":
    # Use Render's assigned PORT, fallback 5000 for local testing
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

