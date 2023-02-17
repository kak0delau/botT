import telebot
import time
from config import TOKEN

bot = telebot.TeleBot(TOKEN)



@bot.message_handler(content_types=["text"])
def text(message):
    if message.text.lower() == "привет":
      bot.sand_message(message.chat.id , "Привет от бота!")
      bot.sand_message(message.chat.id, "Как твои дела? (хорошо/плохо)")
    if message.text.lower() == "хорошо":
      bot.sand_message(message.chat.id , "Супер!")
    if message.text.lower() == "плохо":
      bot.sand_message(message.chat.id, "Печально :(")
bot.polling()