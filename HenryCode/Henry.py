import pyttsx3
import datetime 
import speech_recognition as sr 
import wikipedia #for wikipedia search
import webbrowser #for browsing webpages
import os #for playing music

engine = pyttsx3.init('sapi5') 
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Henry , Please tell me How may i help you ?")


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    # it take microphone input from user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said : {query}\n")
    except Exception as e:
        #print(e)
        print("Say that again please ..... ")
        return "None"
    return query


if __name__=="__main__":
    speak(" jay jay raghuvir samartha")
    wishMe()
    while 1:
        query=takeCommand().lower()

        #logic for executing tasks based on query
        if 'wikipedia' in query: 
            speak("Searching Wikipedia...")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentenses=2)
            speak("According to wikipedia")
            speak(result)
            print(result)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("www.stackoverflow.com")

        elif 'play music' in query:
            music_dir="E:\\Friday Project\\songs"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strtime}")

        elif 'open code' in query:
            codePath="C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)



  