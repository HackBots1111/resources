import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os
from chatterbot.trainers import ListTrainer
import pandas as pd
from chatterbot import ChatBot
import geocoder
from weather import Weather, Unit


# speech converted
r = sr.Recognizer()
r.energy_threshold = 2000

with sr.Microphone() as source:
    print("Speak")
    audio = r.listen(source)
    print('Done')

#considering hindi language as input.
text = r.recognize_google(audio, language = 'hi-IN')
print(text)

translator = Translator()
translated = translator.translate(text, src = 'hi')
#hindi to english done here.
query_to_compute = translated.text

keyword=['weather','price','cost','market']

if keyword[0] in query_to_compute:
	g = geocoder.ip('me')

	weather = Weather(Unit.CELSIUS)
	lookup = weather.lookup_by_latlng(g.latlng[0], g.latlng[1])
	condition = lookup.condition
	answer = condition.text

elif keyword[1] or keyword[2] or keyword[3] in query_to_compute :
	#train market price.
	chatbot = ChatBot("Kabhu")
	data = pd.read_csv('datafile.csv')

	data["key"] = 'price'+ ' '+data["market"].map(str) +' '+ data["commodity"]
	lis =  data["key"].tolist()
	lis2 = data['modal_price'].tolist()
	result = [None]*(len(lis)+len(lis2))
	result[::2] = lis
	result[1::2] = lis2


	chatbot.set_trainer(ListTrainer)
	chatbot.train(result)
	
	#1 weather
	#2 market price 
	answer = chatbot.get_response(query_to_compute)

response = translator.translate(answer, src = 'en', dest = 'hi')
# print(translated.text)


# voice in hindi
voice = gTTS(response.text, lang='hi', slow=False)
print(response.text)
voice.save("speak.mp3")
os.system("mpg321 speak.mp3")



# Solve query here
# return answer


