import speech_recognition as sr
from gtts import gTTS
import pyttsx3

vc = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak to read ")
    audio = vc.listen(source, phrase_time_limit=5)

print("Stop")

try:
    text = vc.recognize_google(audio, language='en')
    print("You said:", text)

    # Using gTTS to convert text to speech
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")

    # Using pyttsx3 to play the saved audio
    engine = pyttsx3.init()
    rate= engine.getProperty('rate')
    engine.setProperty('rate', 150)

    engine.say(text)
    engine.runAndWait()

except sr.UnknownValueError:
    print("I did not understand your words")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
