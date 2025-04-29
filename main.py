import telebot
import os

TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, "Hello! Please send me the Spotify song link.")

@bot.message_handler(func=lambda message: True)
def link_handler(message):
    bot.send_message(message.chat.id, f"Downloading from: {message.text}")
    # Yuklab olish funksiyasi bu yerda yoziladi

bot.polling()
