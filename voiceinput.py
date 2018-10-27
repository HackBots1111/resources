import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os

r = sr.Recognizer()
r.energy_threshold = 5000

with sr.Microphone() as source:
    print("Speak")
    audio = r.listen(source)
    print('Done')

text = r.recognize_google(audio, language = 'hi-IN')
print(text)

translator = Translator()
translated = translator.translate(text, src = 'hi')
print(translated.text)

voice = gTTS(text, lang='hi', slow=False)
voice.save("speak.mp3")
os.system("mpg321 speak.mp3")

