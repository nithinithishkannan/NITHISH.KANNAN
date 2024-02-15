
from gtts import gTTS as gs
from deep_translator import GoogleTranslator as gt
from io import BytesIO
import time
from pygame import mixer
def speak(txt,ln):
    mp3_fp=BytesIO()
    tts=gs(text=txt,lang=ln)
    tts.write_to_fp(mp3_fp)
    return mp3_fp

mixer.init()

lng_code = ['ta','te','hi','kn','en', 'es', 'ml', 'ja', 'mr']
txt="mobile phone prohibated"
for i in lng_code:
    t = gt(source='auto', target=i).translate(txt)
    print(t,i)

    sound=speak(t,i)
    sound.seek(0)
    mixer.music.load(sound,"mp3")
    mixer.music.play()

    time.sleep(2)

