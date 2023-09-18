import telebot

TOKEN = "6358993045:AAEOIycNpWa7ZrsfTuNiIPLj0TXo3FICEUg"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(['start'])
def start(message):
  bot.reply_to(message, "Welcome To Valnoanime")


bot.polling()
