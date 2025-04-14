import os
import requests
from telegram import Bot

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = Bot(token=TELEGRAM_TOKEN)

HELIUS_API_KEY = "66bdb9d8-7d89-45fd-ae8d-cda0f8be13ae"
MONITORED_WALLETS = ["5F8fPL9WBkqZd8nTfZK7rGxzy2R5qKjHwvxPhqP3rFDS"]
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "your_chat_id_here")

def check_transactions():
    for wallet in MONITORED_WALLETS:
        url = f"https://api.helius.xyz/v0/addresses/{wallet}/transactions?api-key={HELIUS_API_KEY}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                for tx in data[:2]:
                    sig = tx.get("signature")
                    amount = tx.get("amount", "N/A")
                    msg = f"صفقة جديدة من المحفظة:
{wallet}
Signature: {sig}
Amount: {amount}"
                    bot.send_message(chat_id=CHAT_ID, text=msg)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    print("WhaleTap AI is monitoring...")
    check_transactions()
