import pyttsx3 # pip install pyttsx3
import datetime
import speech_recognition as sr # pip install speechRecognition
import wikipedia # pip install wikipedia
import webbrowser
import os
import smtplib
import random
import sys

# Here, we import the pyttsx3 module into our program
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') # getting the details of the AI voices available for us
# Here we have imported a Male AI voice for my program. To get a Female AI voice rewrite the below statment as 'engine.setProperty('voice',voices[1].id)' 
engine.setProperty('voice',voices[0].id)

def speak(audio):
    """This function will make our AI talk, by converting the given text argument to speech."""
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    """With this function our AI will wish or greet us, using datetime module"""
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<16:
        speak("Good Afternoon")

    elif hour>=16 and hour<20:
        speak("Good Evening")

    speak("Jarvis here. How may I help you")

def takeCommand():
    """Using speechRecognition module this function will help our AI to take microphone input command from us and will return a string output.""" 
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

def emaiList():
    """This function returns the Email address of the person, to whom, you want to send the mail."""
    emailDict={"friend1":"friend1email@gmail.com","friend2":"friend2email@gmail.com","friend3":"friend3email@gmail.com","friend4":"friend4email@gmail.com"}
    takeCommand()
    specify=query.split(" ")
    myEmail=specify[len(specify)-1]
    print(myEmail)
    return emailDict[myEmail]

def sendEmail(to,content):
    """This function uses smtplib module, to send emails to the recipitent."""
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    f=open("dish.txt","r")
    txt=f.readline()
    server.login('youremail@gmail.com',txt) # 'txt' variable contains the password of your Gmail account. You need to write your password in dish.txt file, so that, it is not directly visible here in Jarvis.py(For security reasons).
    f.close()
    server.sendmail('youremail@gmail.com',to,content)
    server.close()

# Enable 'less secure apps' feature of your gmail account, otherwise the sendEmail function might not work properly

if __name__ == "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            # This condition runs if 'wikipedia' is in the search query. Uses wikipedia module.
            speak('Searching wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=3) # This will store and retrive 3 sentences from perticular wikipedia search. Increase the value of 'sentences' to get more information.
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            # This condition runs if 'open youtube' is in the search query. Uses webbrowser module.
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            # This condition runs if 'open google' is in the search query. Uses webbrowser module.
            webbrowser.open("google.com")

        elif 'open github' in query:
            # This condition runs if 'open github' is in the search query. Uses webbrowser module.
            webbrowser.open("github.com")

        elif 'open linkedin' in query:
            # This condition runs if 'open linkedin' is in the search query. Uses webbrowser module.
            webbrowser.open("linkedin.com")

        # You can automate the opening of any website by writing an elif condition for that, like the above three.

        elif 'the time' in query:
            # This will tell us the time if 'the time' is in the search query. Uses datetime module
            srtTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {srtTime}") 

        elif 'email to' in query:
            # Using the try and except block to handle any possible error while sending email
            try:
                speak('What should I say')
                content = takeCommand()
                to = emaiList()
                print(to)
                sendEmail(to,content)
                speak("Email has been send")
            except Exception as e:
                print(e)
                speak("Sorry email cannot be send")

        elif 'exit' in query:
            # To exit the while loop of this AI, if 'exit' is in query statment. Uses sys module
            sys.exit()

                
