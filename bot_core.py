import telebot
import main

bot = telebot.TeleBot('5227143148:AAG3FA6wv7_GeTIk2NCuDML_aIZ_oD-djHE')


@bot.message_handler(commands=['start'])
@bot.message_handler(commands=['help'])
def get_text_messages(message):
    if message.text.startswith('/start'):
        if (''.join(liter for liter in message.text if (liter.isdigit()))).isdigit():
            bot.send_message(message.from_user.id, main.show_statistic(main.all_heroes, int(''.join(
                liter for liter in message.text if (liter.isdigit())))))
        else:
            bot.send_message(message.from_user.id, main.show_statistic(main.all_heroes))
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


print('im ready!')
bot.polling(none_stop=True, interval=0)
