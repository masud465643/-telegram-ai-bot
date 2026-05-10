import os
import telebot
from openai import OpenAI

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

bot = telebot.TeleBot(BOT_TOKEN)
client = OpenAI(api_key=OPENAI_API_KEY)

@bot.message_handler(func=lambda message: True)
def chat(message):
    user_text = message.text

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": user_text}
        ]
    )

    reply = response.choices[0].message.content

    bot.reply_to(message, reply)

print("AI Bot Running...")
bot.infinity_polling()