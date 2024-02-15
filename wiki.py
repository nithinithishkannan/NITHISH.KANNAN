import pyttsx3
import wikipedia
k=pyttsx3.init()
inings=input("searching wikipedia/google: ")
result=wikipedia.summary(inings,sentences =3)
print(result)
k.say(result)
rate = k.getProperty('rate')
k.setProperty('rate', 150)
k.say(result)
k.runAndWait()
