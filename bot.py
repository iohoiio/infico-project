
import telebot
from telebot import types
import requests

API_TOKEN = '7362462048:AAEiZlTdU4GRGIKW39aD6_dEGD6nS2jowiY'
CHANNEL_USERNAME = '@INFICOTG'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to INFICO Bot!")

# Симуляция базы данных
user_data = {}

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    web_app_info = types.WebAppInfo("https://git.heroku.com/infico.git")  # URL вашего веб-приложенияh
    web_app_button = types.InlineKeyboardButton(text="Open Web App", web_app=web_app_info)
    markup.add(web_app_button)
    bot.send_message(message.chat.id, "Welcome! Click the button below to open the web app.", reply_markup=markup)

@bot.message_handler(content_types=['web_app_data'])
def handle_web_app_data(message):
    data = message.web_app_data.data  # Получение данных из веб-приложения
    user_id = message.from_user.id

    # Обработка данных
    if "action" in data:
        action = data["action"]
        if action == "check_subscription":
            if user_is_subscribed(message.from_user.username):
                bot.send_message(message.chat.id, "You are subscribed! Moving to the next step...")
                bot.send_animation(message.chat.id, 'https://example.com/congratulations.gif')
                show_step2(message)
            else:
                bot.send_message(message.chat.id, "You are not subscribed. Please subscribe to @INFICOTG.")
                bot.send_animation(message.chat.id, 'https://example.com/sad.gif')

def user_is_subscribed(username):
    # Реализуйте логику проверки подписки пользователя
    # Это может включать использование Telegram Bot API для проверки списка участников канала
    response = requests.get(f"https://api.telegram.org/bot{API_TOKEN}/getChatMember?chat_id={CHANNEL_USERNAME}&user_id={username}")
    result = response.json()
    if result['ok'] and result['result']['status'] in ['member', 'administrator', 'creator']:
        return True
    return False

def show_step2(message):
    # Логика для второго шага
    bot.send_message(message.chat.id, "Step 2: Connect your TON Wallet to INFICOBOT.")
    # Дополните шаги и логику проверки кошелька здесь

bot.polling()


