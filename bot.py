bot.py
import telebot

BOT_TOKEN = "8710393332:AAHtd20FWZwqzkk0KLbGi5Tla-dixEeS--Q"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def reply(message):
    bot.reply_to(message, "Message received successfully!")

print("Bot is running...")
bot.infinity_polling()