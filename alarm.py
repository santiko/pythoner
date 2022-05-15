import time
import pyttsx3
from datetime import datetime


def say(text):
	engine = pyttsx3.init()
	voices = engine.getProperty('voices')[1]
	engine.setProperty('voice', voices.id)

	rate = engine.getProperty('rate')
	engine.setProperty('rate', 125)

	engine.say(text)
	engine.runAndWait()

def remember(h, m, s, lt, somthing):

	while True:
		time.sleep(1) #update the time
		current_time = datetime.now()
		hour = current_time.hour - 12
		minut = current_time.minute
		sec = current_time.second
		local_time = current_time.strftime('%p')#return PM or AM


		if hour == h and minut == m and sec == s and local_time == lt:
			say(somthing)


remember(6, 41, 50, 'PM', 'I love you amr')