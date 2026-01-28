from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def predict_fake_news(text):
    fake_words = ["clickbait", "shocking", "unbelievable"]
    return 0 if any(word in text.lower() for word in fake_words) else 1

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    text = data.get("news", "")
    pred = predict_fake_news(text)
    result = "Fake" if pred == 0 else "Real"
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run()
