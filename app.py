from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# 🔥 SUPER ULTRA SHARP FAKE TRIGGERS
FAKE_PHRASES = [
    # clickbait / hype
    "clickbait", "shocking", "unbelievable", "fake", "scam", "alert",
    "breaking", "exclusive", "secret", "surprising", "amazing", "crazy",
    "incredible", "you won't believe", "truth", "hoax", "rumor", "leak",
    "exposed", "must see", "trending", "viral", "scandal", "urgent",
    "sensational", "warning", "false", "fabricated", "bait", "deceptive",
    "fraud", "caught", "fake info", "fake report", "not true", "lies",
    "unverified", "bogus", "dangerous", "fatal", "destroyed", "mystery",
    "impossible", "mind-blowing", "life-changing", "outrageous", "critical",
    "catastrophe", "alert news", "fake leak", "exclusive report",

    # authority / sarcastic
    "doctor confirms", "scientist proves", "expert says", "research shows",
    "study reveals", "nasa hides", "government secret", "breaking discovery",
    "scientists agree", "medical breakthrough", "official statement",
    "authority confirms", "top secret", "official report", "scientific evidence",
    "doctor says", "expert opinion", "medical claim", "scientists discover",
    "research proves", "official announcement", "confirmed by experts",
    "verified by doctors", "doctor recommends", "scientists confirm",
    "doctor claims", "scientific breakthrough", "study confirms",

    # sci-fi / absurd / miracles
    "mars project", "time travel", "aliens exist", "unicorn proven",
    "scientist discovers immortality", "doctor claims flying car",
    "nasa hides portal", "secret teleportation", "robot army",
    "miracle potion", "fountain of youth", "doctor confirms invisibility",
    "scientist proves telepathy", "hidden civilization", "alien technology",
    "magic cure", "miracle weight loss", "doctor says cure cancer instantly",
    "government time machine", "scientist reveals clones",
    "miracle eyesight cure", "magic hair growth", "alien virus",
    "nasa secret mission", "top secret alien files", "scientist proves immortality",
    "doctor confirms perpetual motion", "hidden dimension", "miracle anti-aging",
    "magical elixir", "psychic powers",

    # social media / hype
    "facebook post viral", "tweet goes viral", "instagram trend",
    "tiktok sensation", "viral challenge", "internet sensation",
    "youtube video viral", "reddit hype", "social media hoax",
    "online scam", "viral meme", "trending tweet", "fake influencer",
    "celebrity fake news", "fake quote", "false rumor", "online conspiracy",
    "manipulated video", "photoshopped image", "deepfake", "digital hoax",
    "internet lies", "social media lie", "fake online report", "viral misinformation",
    "click for truth", "share if true", "must share", "fake challenge", "fake giveaway",
]

# 🔥 Function to calculate "sharpness score" based on phrase hits
def predict_fake_news(text):
    text_lower = text.lower()
    count = 0
    for phrase in FAKE_PHRASES:
        if phrase in text_lower:
            count += 1

    # Scoring thresholds
    if count == 0:
        return "Real"
    elif 1 <= count <= 3:
        return "Likely Fake"
    elif 4 <= count <= 7:
        return "Very Likely Fake"
    else:
        return "Extreme Fake Alert"

@app.route("/", methods=["GET"])
def home():
    return "Fake News Detection API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    text = data.get("news", "")

    if text.strip() == "":
        return jsonify({"result": "Please enter some news text"}), 400

    result = predict_fake_news(text)
    return jsonify({"result": result})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

