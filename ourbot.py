import telebot
import re

bot = telebot.TeleBot('1042781969:AAH9kxoyrHi6MaXWLT3ER9d11hQmP9mJ8u8')

@bot.message_handler(content_types=['text'])
def handle_text_messages(message):

    if message.text == "кись":
        bot.send_message(message.chat.id, "Серый-серый-серый-серый-серенький Кись!\nУ него всё очень-очень хорошо!")
        #bot.reply_to(message, "Серый-серый-серый-серый-серенький Кись!\nУ него всё очень-очень хорошо!")
    elif message.text == re.search('мяу +/i', message.text):
        bot.send_message(message.chat.id, "применилась регулярка")
    elif message.text == "мяу1":
        #bot.send_message(message.from_user.id, "мяу")
        #bot.reply_to(message, "мяу")
        #bot.send_sticker(message.chat.id, "CAACAgIAAxkBAALo817b0dwV_AZwTyvKYd4n5Vjv9xKKAAJ6AANb-bUSLcB_10CpHboaBA")
        bot.send_voice(message.chat.id, "AwACAgIAAxkBAAIBQF7ceKypMg7g0p274vklpkb0oOAZAAJVCAAC81vhSrWrdOpc_t76GgQ")

    else:
        bot.send_message(message.chat.id, "Напиши 'кись' чтобы узнать как дела у серого кися")
        #bot.reply_to(message, "Напиши 'кись' чтобы узнать как дела у серого кися")
bot.polling(none_stop=True, interval=0)

