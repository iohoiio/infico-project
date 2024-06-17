import telebot
from telebot import types

BOT_TOKEN = 'AAEiZlTdU4GRGIKW39aD6_dEGD6nS2jowiY'
ADMIN_ID = 358551156
CHANNEL_USERNAME = '@INFICOTG'
CHANNEL_LINK = 'https://t.me/INFICOTG'

bot = telebot.TeleBot(BOT_TOKEN)

users = {}  # временное хранилище пользователей, для реального проекта используйте базу данных

@bot.message_handler(commands=['start'])
def start(message):
    main_menu(message)

def main_menu(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    btn1 = types.KeyboardButton('📄 Apply for ICO')
    btn2 = types.KeyboardButton('🏆 Partner Ranking')
    btn3 = types.KeyboardButton('ℹ About / Tokenomics / FAQ')
    btn4 = types.KeyboardButton('🛒 Digital Store')
    btn5 = types.KeyboardButton('🎁 Get Tokens')
    btn6 = types.KeyboardButton('📁 Partner Content')
    btn7 = types.KeyboardButton('🌟 Influencer Development Fund')
    btn8 = types.KeyboardButton('💼 Advertising / Collaboration')
    btn9 = types.KeyboardButton('📊 Personal Cabinet')
    btn10 = types.KeyboardButton('💰 Donations')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10)
    bot.send_message(message.chat.id, "INFICO - №1 EXCLUSIVELY INFLUENCERS ICO\nMade with LOVE for INFLUENCERS, SUBSCRIBERS and ADVERTISERS\nДоступно WORLDWIDE\nСчетчик розданных токенов (1,000 из 150,000,000,000) и в процентах 13%\nСотрудничество с X, TikTok, Instagram, OnlyFans, Twitch, Facebook, Pinterest, Medium, VK, WeChat.", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == '📄 Apply for ICO')
def apply_for_ico(message):
    step_1(message)

def step_1(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Subscribe to @INFICOTG', url=CHANNEL_LINK)
    btn2 = types.InlineKeyboardButton('Check Subscription', callback_data='check_subscription')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "Шаг 1 из 6\nПодпишитесь на @INFICOTG, После этого вам будет доступна функция ICO!", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'check_subscription')
def check_subscription(call):
    user_id = call.from_user.id
    if check_user_subscription(user_id, CHANNEL_USERNAME):
        bot.send_animation(call.message.chat.id, 'URL_TO_CONGRATULATORY_ANIMATION')
        step_2(call.message)
    else:
        bot.send_animation(call.message.chat.id, 'URL_TO_SAD_ANIMATION')
        bot.send_message(call.message.chat.id, "Вы не подписались на @INFICOTG, Подпишитесь и вы сможете перейти к следующему шагу.")
        step_1(call.message)

def check_user_subscription(user_id, channel_username):
    user_status = bot.get_chat_member(channel_username, user_id).status
    return user_status in ['member', 'administrator', 'creator']

def step_2(message):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton('Connect your TON Wallet', callback_data='connect_wallet')
    markup.add(btn)
    bot.send_message(message.chat.id, "Шаг 2 из 6\nConnect your TON Wallet to INFICOBOT.\nIf you don't have a TON Wallet, go to https://t.me/wallet.", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'connect_wallet')
def connect_wallet(call):
    # Логика подключения TON Wallet пользователя
    # После успешного подключения:
    bot.send_animation(call.message.chat.id, 'URL_TO_CONGRATULATORY_ANIMATION')
    step_3(call.message)

def step_3(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    msg = bot.send_message(message.chat.id, "Шаг 3 из 6\nВведите имя вашего канала:", reply_markup=markup)
    bot.register_next_step_handler(msg, process_channel_name)

def process_channel_name(message):
    channel_name = message.text
    users[message.chat.id] = {'channel_name': channel_name}  # сохраняем имя канала для пользователя
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton('✅ I Agree', callback_data='confirm_channel')
    markup.add(btn)
    bot.send_message(message.chat.id, "Пожалуйста, подтвердите согласие на размещение вашего контента в каналах INFICO", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'confirm_channel')
def confirm_channel(call):
    bot.send_animation(call.message.chat.id, 'URL_TO_CONGRATULATORY_ANIMATION')
    step_4(call.message)

def step_4(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    msg = bot.send_message(message.chat.id, "Шаг 4 из 6\nВведите язык вашего контента:", reply_markup=markup)
    bot.register_next_step_handler(msg, process_language)

def process_language(message):
    language = message.text
    users[message.chat.id]['language'] = language  # сохраняем язык контента для пользователя
    bot.send_animation(message.chat.id, 'URL_TO_CONGRATULATORY_ANIMATION')
    step_5(message)

def step_5(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    msg = bot.send_message(message.chat.id, "Шаг 5 из 6\nВведите до 3 основных тематик вашего контента:", reply_markup=markup)
    bot.register_next_step_handler(msg, process_content_types)

def process_content_types(message):
    content_types = message.text.split(',')
    users[message.chat.id]['content_types'] = content_types  # сохраняем тематики контента для пользователя
    bot.send_animation(message.chat.id, 'URL_TO_CONGRATULATORY_ANIMATION')
    step_6(message)

def step_6(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    msg = bot.send_message(message.chat.id, "Шаг 6 из 6\nУкажите ссылки на ваши социальные сети для идентификации количества подписчиков:", reply_markup=markup)
    bot.register_next_step_handler(msg, process_social_links)

def process_social_links(message):
    social_links = message.text.split(',')
    users[message.chat.id]['social_links'] = social_links  # сохраняем ссылки на соц. сети для пользователя
    bot.send_animation(message.chat.id, 'URL_TO_CONGRATULATORY_ANIMATION')
    send_application_to_admin(message)

def send_application_to_admin(message):
    user_data = users[message.chat.id]
    admin_message = f"Новая заявка на ICO:\nID: {message.chat.id}\nUsername: @{message.from_user.username}\nChannel: {user_data['channel_name']}\nLanguage: {user_data['language']}\nContent Types: {', '.join(user_data['content_types'])}\nSocial Links: {', '.join(user_data['social_links'])}"
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Одобрить', callback_data=f'approve_{message.chat.id}')
    btn2 = types.InlineKeyboardButton('Откорректировать', callback_data=f'correct_{message.chat.id}')
    btn3 = types.InlineKeyboardButton('Сообщение', callback_data=f'message_{message.chat.id}')
    markup.add(btn1, btn2, btn3)
    bot.send_message(ADMIN_ID, admin_message, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith('approve_'))
def approve_application(call):
    user_id = int(call.data.split('_')[1])
    bot.send_message(user_id, "Поздравляем, ваша заявка на ICO одобрена!")
    # Логика начисления токенов

@bot.callback_query_handler(func=lambda call: call.data.startswith('correct_'))
def correct_application(call):
    user_id = int(call.data.split('_')[1])
    bot.send_message(user_id, "Ваша заявка на ICO требует корректировки. Пожалуйста, уточните данные.")
    # Логика корректировки данных

@bot.callback_query_handler(func=lambda call: call.data.startswith('message_'))
def message_application(call):
    user_id = int(call.data.split('_')[1])
    bot.send_message(user_id, "Администратор отправил вам сообщение.")
    # Логика отправки сообщения пользователю

if __name__ == '__main__':
    bot.polling(none_stop=True)
