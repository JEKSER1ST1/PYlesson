# 5276658619:AAGQYunz0P7NXpLuWO7ygmyB6TdXZuEkfsM
import telebot

bot = telebot.TeleBot("5276658619:AAGQYunz0P7NXpLuWO7ygmyB6TdXZuEkfsM")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет меня зовут Бот давай с тобой познакомимся")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    # bot.reply_to(message, message.text)
    if message.text == "привет":
        bot.reply_to(message, "privet rad znakomstvu")
    elif message.text == "как дела":
        bot.reply_to(message, "Нормально")
    elif message.text == "как настроение":
        bot.reply_to(message, "Прекрасно")
    elif message.text == "как себя чувствуешь":
        bot.reply_to(message, "Норм")
    elif message.text == "как день прошел?":
        bot.reply_to(message, "Хорошо!")
    elif message.text == "Как ЗНО":
        bot.reply_to(message, "Страшно")
    elif message.text == "как ЕГЕ":
        bot.reply_to(message, "Весело")
    elif message.text == "Как в шк":
        bot.reply_to(message, "Плохо")
    else:
        bot.reply_to(message, "я не понимаю тебя")

bot.infinity_polling()
