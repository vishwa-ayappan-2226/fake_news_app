from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # allow frontend to call API

# Simple fake news logic with lots of trigger words
FAKE_WORDS = [
    "clickbait","shocking","unbelievable","fake","scam","breaking",
    "amazing","miracle","secret","hidden","government","alert",
    "urgent","viral","shocker","hoax","cure","instant","double","win",
    "money","rich","hidden","exposed","conspiracy","truth","lies",
    "banned","illegal","exclusive","breaking news","secret formula"
]

def predict_fake_news(text):
    # Return 0 for Fake, 1 for Real
    text_lower = text.lower()
    return 0 if any(word in text_lower for word in FAKE_WORDS) else 1

@app.route("/", methods=["GET"])
def home():
    return "Fake News Detection API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    text = data.get("news", "")

    if not text.strip():
        return jsonify({"result": "Please enter some news text"}), 400

    try:
        pred = predict_fake_news(text)
        result = "Fake" if pred == 0 else "Real"
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"result": "Error processing request", "error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

