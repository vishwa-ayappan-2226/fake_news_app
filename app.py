from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

FAKE_PHRASES = [

    # 🚨 clickbait & hype
    "clickbait","shocking","unbelievable","breaking","secret revealed",
    "must watch","must see","you won't believe","exposed truth",
    "hidden truth","viral news","urgent alert","big reveal","sensational",

    # 💊 medical & miracle scams
    "miracle cure","cure cancer instantly","doctor confirms cure",
    "one drink cures","no medicine needed","heal overnight",
    "weight loss in days","grow hair fast","reverse diabetes",
    "never fall sick","medical breakthrough miracle",
    "scientists found cure for all diseases",

    # 🏛 government & money rumors
    "government giving free money","free cash scheme","bank doubles money",
    "atm will stop working","new secret tax rule","hidden gold reserve",
    "government hiding truth","big government secret","new rule tomorrow",

    # 👽 sci-fi & impossible
    "aliens found","alien invasion","mars colony next year",
    "time travel discovered","humans immortal","teleportation invented",
    "secret portal found","living underwater","flying cars released",

    # 📱 internet scams
    "share to win money","click to earn","free recharge forever",
    "whatsapp trick","new app gives free money","instant profit scheme",
    "investment doubles in week","crypto guaranteed profit",

    # 🎭 fake authority claims
    "scientists confirm","doctors shocked","experts reveal",
    "study proves overnight","official leak","top secret report",
    "research confirms miracle","medical experts stunned",

    # 🤯 extreme exaggeration
    "world will end soon","dead rise again","sun will stop shining",
    "earth will split","humans can fly now","gravity turned off",

    # 📢 misinformation words
    "hoax","fake report","false claim","fabricated story",
    "unverified source","misleading news","rumor spreading",
    "conspiracy theory","manipulated video","deepfake footage"
]


def analyze_news(text):
    text = text.lower()
    hits = sum(1 for phrase in FAKE_PHRASES if phrase in text)

    if hits == 0:
        return "Real", 90
    elif hits == 1:
        return "Fake", 75
    elif hits == 2:
        return "Fake", 85
    elif hits == 3:
        return "Fake", 92
    else:
        return "Fake", 97


@app.route("/")
def home():
    return "Fake News Detection API Running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    news = data.get("news","")

    if not news.strip():
        return jsonify({"result":"Empty"}),400

    result, confidence = analyze_news(news)

    return jsonify({
        "result": result,
        "confidence": confidence
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

