import os
import requests
from flask import Flask, request

app = Flask(__name__)
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    if "message" in data and "text" in data["message"]:
        chat_id = data["message"]["chat"]["id"]
        text = "WhaleTap bot is active and received your message!"
        requests.post(f"{API_URL}/sendMessage", json={"chat_id": chat_id, "text": text})
    return {"ok": True}

if __name__ == "__main__":
    app.run(debug=True)