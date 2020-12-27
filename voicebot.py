import requests
import pyttsx3
import speech_recognition as sr    #import the library
from gtts import gTTS
import os
import playsound
import random

    # initialize recognizer
def botSpeak(audiostring):
    text_to_speech=gTTS(text=audiostring,lang="en")
    r=random.randint(0,10*3)
    voice_file='voice-'+str(r)+'.mp3'
    text_to_speech.save(voice_file)
    print(audiostring)
    playsound.playsound(voice_file)
    os.remove(voice_file)

def record_audio():
    with sr.Microphone() as source:
        # Mention source it will be either in Microphone or audio
        print("Speak Anything...")
        audio1 = r.listen(source)
        # listen to source
        text=''
        try:
            text = r.recognize_google(audio1)  # use recognizer to convert our audio into text
            print(f"You said :{text}")
        except sr.UnknownValueError:
                botSpeak("Sorry, that didn't come up right please try again!")
        except sr.RequestError:
                botSpeak('sorry,my speech service is down')

    return text

r=sr.Recognizer()
botmessage=""
while botmessage!='Bye':
    message = record_audio()
    print(f'message=={message}')
    response = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": message}).json()
    print('Bot speak....')
    for i in response:
        try:
            botmessage=i['text']
            print(f'botmessage=={botmessage}')

        except:
            botmessage=i['image']
            print(i['image'])

#     r=requests.post('http://localhost:5002/webhooks/rest/webhook',json={"sender":sender,"message":message}).json()


# rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml
# the above command is used to run rasa from external python code



























