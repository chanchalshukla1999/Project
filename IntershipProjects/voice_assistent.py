import speech_recognition as sr
import wikipedia
import pyttsx3
import datetime

# Step1.initalize the speech regonition in any variable
r = sr.Recognizer()

# Step2.intialize the text-to-speech engine
engine  = pyttsx3.init()

#Step3.Voice assistant functions

def Hello_fun():
    engine.say("Hello! How can I help you?")
    engine.runAndWait()

def Time_fun():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    engine.say("The current time is"+current_time)
    engine.runAndWait()

def Date_fun():
    current_date = datetime.datetime.now().strftime("%B %d, %Y")
    engine.say("Todays date is" +current_date)
    engine.runAndWait()

def Search_fun(query):
    try:
        result = wikipedia.summary(query, sentences = 2)
        engine.say(result)
        engine.runAndWait()
    except wikipedia.exceptions.DisambiguationError as e:
        engine.say("Please check your keyword" + query)
        engine.runAndWait()

# Step4.creating loop for listening voice command continueously
while True:
    with sr.Microphone() as source:
        print("Listening....")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio, language="en-US")
        print("You Said:" + command)

        if "hello" in command.lower():
            Hello_fun()
        elif "time"in command.lower():
            Time_fun()
        elif "date" in command.lower():
            Date_fun()
        else:
            Search_fun(command)
    except sr.UnknownValueError:
        print("Sorry,I did not get")
    except sr.RequestError as e:
        print("Error;{0}".format(e))
