# Importing packages
import warnings
import pyttsx3  
import speech_recognition as sr
import smtplib
import os
import datetime
import calendar
import random
import subprocess
import webbrowser
import wikipedia
import pywhatkit
from selenium import webdriver

warnings.filterwarnings("ignore")
# Making text to speech engine
engine = pyttsx3.init()

# Giving voice to our assistant
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[0].id)   #changing index, changes voices. 1 for female
 
 
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

def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])
##

def send_email(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()

    # Enable low security in gmail
    server.login("nairaditya2003@gmail.com", "zzjhccdkqageyzte")
    server.sendmail("nairaditya2003@gmail.com", to, content)
    server.close()


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
    return f'Today is {week_now},{months[month_now -1]} ,{ordinals[day_now-1]}.'
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
            
        elif "open" in text.lower():
            if "chrome" in text.lower():
                speak = speak + "Opening Google Chrome"
                talk(speak)
                os.startfile(
                    r"C:\Program Files\Google\Chrome\Application\chrome.exe"
                )
        
            elif "youtube" in text.lower():
                speak = speak + "Opening Youtube\n"
                talk("Opening Youtube")
                print("Jarvis : Opening Youtube")
                webbrowser.open("https://youtube.com/")
                    
            # Search
            elif "google" in text.lower():
                talk("What do you want to search in Google?")
                print("Jarvis: What do you want to search in Google?")
                search = get_Audio()
                print("Jarvis : Opening Google")
                talk("Opening Google")
                search_query_encoded = "+".join(search.split())
                search_url = f"https://www.google.com/search?q={search_query_encoded}"
                webbrowser.open(search_url)
                print(f"Jarvis : Opening {search} in Google.")
                talk(f"Opening {search} in Google")
            
            elif "word" in text.lower():
                    speak = speak + "Opening Microsoft Word"
                    print("Jarvis : " +speak)
                    talk(speak)
                    os.startfile(
                        r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.exe"
                    )

            elif "excel" in text.lower():
                speak = speak + "Opening Microsoft Excel"
                print("Jarvis : " +speak)
                talk(speak)
                os.startfile(
                    r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE"
                )
            
            elif "powerpoint" in text.lower():
                speak = speak + "Opening Microsoft PowerPoint"
                print("Jarvis : " +speak)
                talk(speak)
                os.startfile(
                    r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE"
                )
                
        elif "email" in text or "gmail" in text or "mail" in text:
            try:
                talk("What should I say")
                print("Jarvis : What should I say ?")
                content = get_Audio()
                talk("Enter Receivers Email")
                to = input("Jarvis : Enter Receivers Email : ")
                send_email(to,content)
                speak = speak + "Email Has Been Sent"
                print("Jarvis : Email Has Been Sent")
                talk(speak)
            except Exception as e:
                print(e)
                print("Jarvis : I am not able to sent this email")
                talk("I am not able to sent this email")
        
        elif "set reminder" in text.lower(): 
            print("Jarvis : What do you want me to remember ? ")
            talk("What do you want me to remember?")
            msg = get_Audio()
            talk("You asked me to remind you that : " +msg)
            print("Jarvis : You asked me to remind you that : " +msg)
            rem_file = open('reminder.txt','a')
            rem_file.write(msg)
            rem_file.close()
            print("Jarvis : Reminder Saved")
            talk("Reminder Saved")
        
        elif "show reminders" in text.lower():
            with open('reminder.txt', 'r') as rem_file:
                print("Jarvis: These Are Your Reminders")
                reminders = rem_file.read()
                print(reminders)
                talk("These Are Your Reminders: " + reminders)

        elif "play music" in text.lower():
            print("Jarvis : Which song you want me to play?")
            talk("Which Song You Want me to play")
            song = get_Audio()
            print("Jarvis : Playing " + song)
            talk("Playing " + song)       
            pywhatkit.playonyt(song)
        
        elif "take notes" in text.lower():
            print("Jarvis : Tell Me  ")
            talk("Tell Me")
            msg = get_Audio()
            notes_file = open('notes.txt','a')
            notes_file.write(msg)
            notes_file.close()
            print("Jarvis : Notes Saved")
            talk("Notes Saved")
            
        elif "show notes" in text.lower():
            print("Jarvis : Here Are Your Notes  ")
            talk("Here Are Your Notes")
            notes_file = open('notes.txt','r')
            notes = notes_file.read()
            print(notes)
            notes_file.close()
            
        # Exit the program
        elif "exit" in text.lower():
            print("Jarvis : Goodbye!")
            talk("Goodbye!")
            break
             
    except:
        talk("I don't know that")
            