import json
import telebot

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
bot = telebot.TeleBot('7975464552:AAFhur8cQBQO-EFuvZ_g86YBcZxe8ZCJ79U')

# Загрузка списка пользователей из JSON-файла
def load_users():
    with open('user_data.json', 'r') as file:
        users = json.load(file)
    return users

# Обработчик сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text.startswith('Внимание!'):
        text_information = message.text[9:]
        users = load_users()
        for user_id in users:
            try:
                bot.send_message(user_id, text_information)
            except Exception as e:
                print(f"Не удалось отправить сообщение пользователю {user_id}: {e}")

# Запуск бота
bot.polling(none_stop=True)