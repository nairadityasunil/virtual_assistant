# Importing packages
import warnings
import pyttsx3  
import pyaudio
import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import datetime
import calendar
import random
import wikipedia


warnings.filterwarnings("ignore")
# Making text to speech engine
engine = pyttsx3.init()

# Giving voice to our assistant
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

# Function to make engine talk
def talk(audio):
    engine.say(audio)
    engine.runAndWait()
##

# Function to receive audio from the user
def get_Audio():
    record = sr.Recognizer()
    
    # Using microphone to get audio input
    with sr.Microphone() as source:
        print("\n")
        print("Listening : ")
        audio = record.listen(source)
        
        # Using google speech recognition to recognise the speech
        data = " "
        try:
            data = record.recognize_google(audio)
        
        except sr.UnknownValueError:
            talk("Unable To Understand")
            print("Unable To Understand")
            return " "
        
        except sr.RequestError as e:
            talk("Error From Google Speech Recognition")
            print("Error From Google Speech Recognition")
            return " "
        
        print("Lucifer : "+data)
        return data
##


def response(text):
    print(text)
    tts = gTTS(text=text,lang="en")
    audio = "Audio.mp3"
    tts.save(audio)
    playsound.playsound(audio)
    os.remove(audio)
##

# Making wake word for the assistant
def call(text):
    call_assistant = "jarvis"
    text = text.lower()
    if call_assistant in text:
        return True
    
    return False
##

def get_today():
    # Get current date time
    now = datetime.datetime.now()
    date_now = datetime.datetime.today()
    week_now = calendar.day_name[date_now.weekday()]
    month_now = now.month
    day_now = now.day
    
    months = ['January','February', 'March', 'April', 'May', 'June','July', 'August', 'September', 'October', 'November', 'December']

    ordinals = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10','11', '12', '13', '14', '15', '16', '17', '18', '19', '20','21', '22', '23', '24', '25', '26', '27', '28', '29', '30','31']
    return f'Today is {week_now},{months[month_now -1]} the{ordinals[day_now-1]}.'
##

def greet(text):
    greetings = [
        "hello",
        "hi",
        "hey",
        "how are you?"
    ]
    
    response = [
        "Hello",
        "Hi",
        "Hey",
    ]
    
    for word in text.lower().split():
        if word in greetings:
            return random.choice(response)

    return ""
##

def wiki(text):
    # Convert the input text to lowercase for case insensitivity
    text_lower = text.lower()
    
    if "who is" in text_lower:
        # Find the index of "who is" in the lowercased text
        index = text_lower.find("who is")
        if index != -1:
            # Extract the term following "who is"
            return text[index + len("who is"):].strip()

    elif "what is" in text_lower:
        # Find the index of "what is" in the lowercased text
        index = text_lower.find("what is")
        if index != -1:
            # Extract the term following "what is"
            return text[index + len("what is"):].strip()

    return None  # Return None if no valid query pattern is found
##

name = "Lucifer"
print("Jarvis : Hello "+name)
talk("Hello "+name)            
while True:
    try:
        text = get_Audio()
        speak = ""
    # print(text)
        if call(text):
            speak = speak + greet(text)
            print("Jarvis : "+speak+ " " + name)
            talk(speak + name)
    
        elif ("date" in text) or ("day" in text) or ("month" in text):
            today = get_today()
            speak = speak + today
            print("Jarvis : "+speak)
            talk(speak)
        
        elif "time" in text:
            current_time = datetime.datetime.now()
            meridiem = ""
        
            if current_time.hour >= 12:
                meridiem = "p m"
                hour = current_time.hour - 12
            else:
                meridiem = "a m"
                hour = current_time.hour
        
            minute = str(current_time.minute)
            speak = speak + "the time is " + str(hour) + " " + minute + " " + meridiem
            print("Jarvis : "+speak)
            talk(speak)
        
        elif "wikipedia" in text or "Wikipedia" in text: 
            print("Jarvis : What do you want to search in wikipedia ?")
            talk("What do you want to search in wikipedia ?")
            search = get_Audio()
            if "who is" in text:
                person = wiki(text)
                info = wikipedia.summary(person,sentences=2)
                speak = speak + info
                print("Javis : "+speak)
                talk(speak)
            else:
                person = wiki(search)
                info = wikipedia.summary(person,sentences=2)
                speak = speak + info
                print("Jarvis : "+speak) 
                # talk(speak)
                talk(speak)
        
        
        # Exit the program
        elif "bye" in text.lower():
            print("Jarvis : Goodbye!")
            talk("Goodbye!")
            break
            
    except:
        talk("I don't know that")
            