import time
import telebot

# создаем бота
bot = telebot.TeleBot('5764218789:AAGg6gdv1O1jryNoL7i2_IKPmIPj951ZD3Y')
# привязка к адресу начинается через @
CHANAL_NAME = '@jokes_gen'

# данные из файла
f = open('data/jokes.txt', 'r', encoding = 'UTF-8')
jokes = f.read().split('\n')
f.close()

# Пока не закончаться шутки, послаем в канал
for joke in jokes:
    bot.send_message(CHANAL_NAME, joke)
    # Пауза раз в час
    time.sleep(30)

bot.send_message(CHANAL_NAME, 'Анекдоты кончились')