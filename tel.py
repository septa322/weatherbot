# -*- coding: utf-8 -*-
import telebot
import pyowm
owm = pyowm.OWM('6d00d1d4e704068d70191bad2673e0cc',language = "ru")
bot = telebot.TeleBot('1051825329:AAGytl8pxgyhvm3EB2tvHRNnmHBsxCelmzw')

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
	observation = owm.weather_at_place(message.text)
	w = observation.get_weather()
	temp = w.get_temperature('celsius')["temp"]
	answer = "В " +  message.text[:-1] + "e " + "сейчас " +  w.get_detailed_status() + "\n"
	answer1 = "В " + message.text[:-1] + "e " + str(temp) + " градусов" + "\n"
	bot.send_message(message.chat.id,answer)
	bot.send_message(message.chat.id,answer1)

bot.polling(none_stop=True, timeout=123)