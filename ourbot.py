import telebot 

bot = telebot.TeleBot('1042781969:AAH9kxoyrHi6MaXWLT3ER9d11hQmP9mJ8u8')

@bot.message_handler(content_types=['text'])
def handle_text_messages(message):

    last_update = bot.get_last_update()
    last_chat_id = last_update['message']['chat']['id']

    if message.text == "кись":
        bot.send_message(last_chat_id, "Серый-серый-серый-серый-серенький Кись!")
        bot.send_message(last_chat_id, "У него всё очень-очень хорошо!")
        #bot.send_message(message.from_user.id, "Серый-серый-серый-серый-серенький Кись!")
        #bot.send_message(message.from_user.id, "У него всё очень-очень хорошо!")
        #bot.reply_to(message, "Серый-серый-серый-серый-серенький Кись!")
        #bot.reply_to(message, "У него всё очень-очень хорошо!")
    elif message.text == "мяу":
        bot.send_message(last_chat_id, "мяу")
        #bot.send_message(message.from_user.id, "мяу")
        #bot.reply_to(message, "мяу")
    else:
        bot.send_message(last_chat_id, "Напиши 'кись' чтобы узнать как дела у серого кися")
        #bot.send_message(message.from_user.id, "Напиши 'кись' чтобы узнать как дела у серого кися")
        #bot.reply_to(message, "Напиши 'кись' чтобы узнать как дела у серого кися")
bot.polling(none_stop=True, interval=0)
