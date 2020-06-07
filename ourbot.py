import telebot
import re
import random


bot = telebot.TeleBot('1042781969:AAH9kxoyrHi6MaXWLT3ER9d11hQmP9mJ8u8')

@bot.message_handler(content_types=['text'])
def handle_text_messages(message):

    if re.search("спой", message.text, re.IGNORECASE):

        songList = ["Серый-серый-серый-серый-серенький Кись!\nУ него всё очень-очень хорошо!", "почему доволен серенький кись?\nпотому что у кися есть серый мись!",
        "серый серый серый кись\nс серыми мисями\nсерый серый серый кись\nснится мне ночами"]

        bot.send_message(message.chat.id, random.choice(songList))
        #bot.reply_to(message, "Серый-серый-серый-серый-серенький Кись!\nУ него всё очень-очень хорошо!")
    elif re.search("мяу", message.text, re.IGNORECASE):
        bot.send_message(message.chat.id, "применилась регулярка")
    elif re.search("миу", message.text, re.IGNORECASE):
        #bot.send_message(message.from_user.id, "мяу")
        #bot.reply_to(message, "мяу")
        #bot.send_sticker(message.chat.id, "CAACAgIAAxkBAALo817b0dwV_AZwTyvKYd4n5Vjv9xKKAAJ6AANb-bUSLcB_10CpHboaBA")
        bot.send_voice(message.chat.id, "AwACAgIAAxkBAAIBQF7ceKypMg7g0p274vklpkb0oOAZAAJVCAAC81vhSrWrdOpc_t76GgQ")

    else:
        bot.send_message(message.chat.id, "Напиши 'спой' чтобы послушать одну из песенок про серого кися")
        #bot.reply_to(message, "Напиши 'кись' чтобы узнать как дела у серого кися")
bot.polling(none_stop=True, interval=0)

