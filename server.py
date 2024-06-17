from flask import Flask, request, jsonify
import telebot

app = Flask(__name__)
BOT_TOKEN = 'YOUR_BOT_TOKEN'
bot = telebot.TeleBot(BOT_TOKEN)

@app.route('/apply_ico', methods=['POST'])
def apply_ico():
    user_id = request.json.get('user_id')
    bot.send_message(user_id, "Starting ICO application process...")
    return jsonify({"status": "success"}), 200

# Аналогичные маршруты для остальных кнопок

if __name__ == '__main__':
    app.run(debug=True)
