import telebot 

bot = telebot.TeleBot('1042781969:AAH9kxoyrHi6MaXWLT3ER9d11hQmP9mJ8u8')

@bot.message_handler(content_types=['text'])
def handle_text_messages(message):
    if message.text == "кись":
        bot.send_message(message.from_user.id, "Серый-серый-серый-серый-серенький Кись!")
        bot.send_message(message.from_user.id, "У него всё очень-очень хорошо!")
    else:
        bot.send_message(message.from_user.id, "Напиши 'кись' чтобы узнать как дела у серого кися" )
bot.polling(none_stop=True, interval=0)