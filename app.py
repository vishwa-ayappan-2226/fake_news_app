from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# -------------------------------
# FAKE NEWS PHRASE DATABASE
# -------------------------------

strong_fake = [
    "clickbait", "shocking", "unbelievable", "you won't believe",
    "fake news", "scam", "hoax", "breaking shocking",
    "must watch", "this will change your life",
    "secret revealed", "exposed truth"
]

money_fake = [
    "get rich quick", "overnight millionaire", "easy passive income",
    "secret investment strategy", "guaranteed returns",
    "risk free trading", "turn 100 into 10000",
    "crypto pump", "next bitcoin",
    "double money in one day",
    "instant profit system"
]

health_fake = [
    "cure all diseases", "100 percent cure",
    "miracle remedy", "heal naturally in days",
    "reverse aging", "never get sick again",
    "magic pill", "one herb cures everything",
    "heal cancer without treatment"
]

conspiracy_fake = [
    "secret government plan", "media hiding the truth",
    "aliens among us", "world ending soon",
    "hidden agenda exposed",
    "mind control technology",
    "fake moon landing proof"
]

giveaway_fake = [
    "congratulations you are selected",
    "claim reward now",
    "free phone offer",
    "you have been chosen",
    "gift waiting for you",
    "exclusive winner"
]

celebrity_fake = [
    "celebrity death confirmed secretly",
    "shocking celebrity scandal",
    "celebrity arrested overnight",
    "secret affair leaked",
    "celebrity hospitalised suddenly"
]

# Combine all fake phrases
all_fake_phrases = (
    strong_fake +
    money_fake +
    health_fake +
    conspiracy_fake +
    giveaway_fake +
    celebrity_fake
)

# -------------------------------
# SMART DETECTION LOGIC
# -------------------------------

def predict_fake_news(text):
    text = text.lower()
    score = 0

    for phrase in all_fake_phrases:
        if phrase in text:
            score += 1

    # Decision based on score
    if score >= 4:
        return "Fake"
    elif score >= 2:
        return "Suspicious"
    else:
        return "Likely Real"


# -------------------------------
# ROUTES
# -------------------------------

@app.route("/", methods=["GET"])
def home():
    return "Fake News Detection API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("news", "")

    if text.strip() == "":
        return jsonify({"result": "Please enter some news text"}), 400

    result = predict_fake_news(text)

    return jsonify({"result": result})


# -------------------------------
# RUN SERVER
# -------------------------------

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

