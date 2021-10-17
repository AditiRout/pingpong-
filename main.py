import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import urllib.request
import urllib.parse
import re
import pywhatkit as pk
import random
import os



engine  = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)
def speak(audio):
    engine.say(audio) #to speak
    engine.runAndWait()

def wishme():
    hour =int(datetime.datetime.now().hour)
    minutes=int(datetime.datetime.now().minute)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening!")

    speak("I  am  luna ")
    speak( "mam Please  tell  me  how  may  I  help  you")


def takecommand():
    #here takes input from user and output given in string can use energy threhold for noise reduction incraese it
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        
        
        r.pause_threshold = 1 #phrase completion time
        r.energy_threshold=6000
        r.dynamic_energy_threshold = True   #noise reduction
        audio=r.listen(source)

    try:#chances of error present
        print("Recognizing..")
        query=r.recognize_google(audio,language="en-in")
        print(f"User said:{query}\n")

    except Exception as e:
        #print(e) for error
        print("Say it again please...")
        return "None"
    return query






if __name__ =="__main__":
    wishme()
    while True:
        query=takecommand().lower()
        if"luna"in query:
            query=query.replace("luna","")
        path="C:/Program Files/Google/Chrome/Application/chrome.exe %s"
        if "wikipedia" in query:
            speak("Searching Wikipedia..")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=4)
            speak("According to Wikipedia")
            speak(results)

        elif "open youtube"in query:
            speak("Opening Youtube..")
            webbrowser.get(path).open("youtube.com")
            speak("What would you like to search in youtube?")
            query_string=takecommand().lower()
            speak("Searching in youtube...")
            html_content = urllib.request.urlopen("http://www.youtube.com/results?search_query="+query_string)
            search_results = re.findall(r"watch\?v=(\S{11})", html_content.read().decode())
            #print(search_results) gives the total links available we can choose any no.
            '''
            speak("Would you like me to play the first video?..")
            ans=takecommand().lower()
            speak("ok..")
            if "yes"in ans:
                    t=("http://www.youtube.com/watch?v=" + search_results[0])
                    webbrowser.get(path).open(t)
            '''
            speak("Would you like me to play any video?..")
            ans=takecommand().lower()
            speak("ok..")
            if "yes"in ans:
                    t=("http://www.youtube.com/watch?v=" + random.choices(search_results))
                    webbrowser.get(path).open(t)

        elif "open google"in query:
            speak("Opening Google..")
            webbrowser.get(path).open("google.com")
            speak("what would you like to search in google?...")
            ans=takecommand().lower()
            if"yes"in ans:
                 speak("Searching in google...")
                 webbrowser.get(path).open("http://www.google.com/search?q="+ans)
            else :
                speak("ok..")

           
            
            #pk.search(ans)
        elif "open github"in query:
            speak("Opening github..")
            webbrowser.get(path).open("github.com")
        elif "open leetcode"in query:
            speak("Opening Leetcode..")
            webbrowser.get(path).open("leetcode.com")
        elif "open instagram"in query:
            speak("Opening Instagram..")
            webbrowser.get(path).open("instagram.com")
        elif "open gmail"in query:
            speak("Opening gmail..")
            webbrowser.get(path).open("gmail.com")
        elif "open whatsapp"in query:
            speak("Opening whatsapp..")
            os.startfile("C:/Users/Asus/Downloads/WhatsAppSetup.exe")
        elif "open figma"in query:
            speak("Opening figma..")
            os.startfile("C:/Users/Asus/AppData/Local/Figma/Figma.exe")
        elif "open discord"in query:
            speak("Opening discord..")
            os.startfile("C:/Users/Asus/AppData/Local/Discord/Update.exe --processStart Discord.exe")
       

        elif"play music"in query:
            speak("What would you like to listen?..")
            ans=takecommand().lower()
            pk.playonyt(ans)

        elif"what is the time now"in query:
            str=datetime.datetime.now().strftime("%I:%M %p")
            speak("current time is "+ str)
           

       
       


        





