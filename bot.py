import telebot

BOT_TOKEN = "8710393332:AAHtd20FWZwqzkk0KLbGi5Tla-dixEeS--Q"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello! Bot is working.")

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, f"You said: {message.text}")

print("Bot started successfully...")
bot.infinity_polling()