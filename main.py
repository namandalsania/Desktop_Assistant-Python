from unittest import result
import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os
import smtplib

print("Initializing Champak")
MASTER = "Jetha"   

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Speak function will pronounce the string which is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()
    
# This function will wish you as per the current time
def wishMe():
    hour = datetime.datetime.now().hour
    
    if hour >= 0 and hour < 12:
        speak("Good Morning" + MASTER)
    
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon" + MASTER)
        
    else:
        speak("Good Evening" + MASTER)
        
    speak("I am Champaklal Jayantilal Gada. How may I help you ?")
     
# this function will take command from the microphone
def takeCommand():   
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        
    except Exception as e:
        print("Say that again please")
        query = None
        
    return query 

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.echo()
    server.starttls()
    server.login('youremail@gmail.com', 'password')  # change while running the code
    server.sendmail("naman@google.com", to, content)
    server.close()

# Main Program starts here
def main():

    speak("Initializing Champak...")
    wishMe()
    query = takeCommand()

    # Logic for executing tasks as per the query
    if 'wikipedia' in query.lower():
        speak("Searching wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        print(results)
        speak(results)

    elif 'open youtube' in query.lower():
        # webbrowser.open("youtube.com")
        url = "youtube.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open google' in query.lower():
        # webbrowser.open("youtube.com")
        url = "google.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open F1' in query:
        # webbrowser.open("youtube.com")
        url = "formula1.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'play music' in query.lower():
        songs_dir = "Music" # songs_dir should contain the path of Music directory
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[0]))

    elif 'the time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{MASTER} the time is {strTime}")

    elif 'open code' in query.lower():
        codePath = "C:\\Users\\naman\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)

    elif 'email to Babita' in query.lower():
        try:
            speak("What should I send")
            content = takeCommand()
            to = receiver@gmail.com  # change while running the code
            sendEmail(to, content)
            speak("Email has been sent successfully")
        except Exception as e:
            print(e)
            
main()

        
                                       

                                               
    

    

    


    
    
