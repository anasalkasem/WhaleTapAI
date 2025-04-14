import os
import requests
from flask import Flask, request

app = Flask(__name__)

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

@app.route('/', methods=["POST"])
def webhook():
    data = request.get_json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        # رد مبدئي على أي رسالة
        message = "أهلاً بك في WhaleTap! أرسل لي عنوان محفظة وسأعطيك تفاصيلها قريباً."

        # إرسال الرد للمستخدم
        requests.post(API_URL, json={
            "chat_id": chat_id,
            "text": message
        })

    return {"ok": True}

@app.route('/')
def home():
    return "WhaleTap bot is online!"

if __name__ == "__main__":
    app.run(debug=True)
