
from fileinput import close
from logging import exception
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
from datetime import date
import sys
import wmi

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour < 12 :
        speak('Good morning, Sir Johny')
    elif hour > 12 and hour <=16 :
        speak('Good After Noon, Sir Johny')
    elif hour > 16 and hour <=24 :
        speak('Good Evening , sir Johny')
    else :
        speak('Hello Sir , Johny')
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source :
        print('Listening...')
        r.pause_threshold = 1
        r.energy_threshold = 100
        audio = r.listen(source)

    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print('user said : ', query)
    except Exception as e :
        #print(e)

        print('Say that again!')
        return "None"
    return query

if __name__ == "__main__" :
    greet()
    #while True:
    while True :
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query , sentences=2)
            speak(' According to wikipedia ')
            print(results)
            speak(results)
        elif 'open youtube' in query:
            speak('Opening Youtube')
            webbrowser.open('Youtube.com')
        elif 'time now' in query:
            time = datetime.datetime.now().strftime("%H:%M")
            speak(f'Sir, the time is {time}')
        elif 'day today' in query:
            day = datetime.datetime.today().weekday() + 1
     
            Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',
                4: 'Thursday', 5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
            if day in Day_dict.keys():
                day_of_the_week = Day_dict[day]
                print(day_of_the_week)
                speak("The day is " + day_of_the_week)

        elif 'open discord' in query:
            speak('Opening discord')
            Discord = 'C:\\Users\\Johny Bhiduri\\AppData\\Local\\Discord\\app-1.0.9005\\Discord.exe'
            os.startfile(Discord)
            
        elif 'open vs code' in query :
            speak('opening vs code')
            Code = 'C:\\Users\\Johny Bhiduri\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(Code)

        elif 'open telegram' in query:
            speak('opening telegram')
            Telegram = 'C:\\Users\\Johny Bhiduri\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe'
            os.startfile(Telegram)
        
        elif 'open whatsapp' in query:
            speak('opening whatsapp')
            whatsapp = 'C:\\Program Files\WindowsApps\\5319275A.WhatsAppDesktop_2.2226.6.0_x64__cv1g1gvanyjgm\\app\\WhatsApp.exe'
            os.startfile(whatsapp)

        elif 'about me' in query:
            with open('Johny.txt') as f:
                k = f.read()
            speak(k)
        
        elif 'quit' in query:
            speak('Quitting Now, Bye Bye')
            exit()
            close()
        

        
        
        
        

        