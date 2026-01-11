import speech_recognition as sr # Import speech recognition library to capture voice input
import webbrowser # Import webbrowser to open websites via voice commands
import pyttsx3 # Import pyttsx3 for offline text-to-speech
import musicLibrary # Import custom music library module
import requests # Import requests to fetch news data from News API
from openai import OpenAI # Import OpenAI client to interact with AI model
from gtts import gTTS # Import gTTS (Google Text To Speech) for better voice quality
import pygame # Import pygame to play MP3 audio files
import os# Import OS module to manage files
import client
recognizer = sr.Recognizer() # Create a recognizer object to recognize speech
engine = pyttsx3.init() # Initialize pyttsx3 speech engine
# Initialize Pygame audio mixer
pygame.mixer.init()
newsapi = "PUT YOUR API Key " # Store News API key

def speak_old(text):   # Function to speak using offline pyttsx3 engine
    engine.say(text)
    engine.runAndWait()

def speak(text):     # Function to speak using Google TTS (more natural voice)
    tts = gTTS(text)
    tts.save('temp.mp3') 
    
    pygame.mixer.music.load('temp.mp3')  # Load the MP3 file
    
    pygame.mixer.music.play()           # Play the MP3 file
    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    # Stop using the current audio file and free the mixer and delete temporary MP3 file after playback to save storage
    pygame.mixer.music.unload() 
    os.remove("temp.mp3") 

def aiProcess(command):        
    # Send the user's command to the AI engine (client.py) and return Jarvis's intelligent response
    return client.ask_jarvis(command)

def processCommand(c):    # Function to process user voice commands
    if "open google" in c.lower():   # Check for website opening commands....
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open github" in c.lower():
        webbrowser.open("https://github.com")
    elif "open netflix" in c.lower():
        webbrowser.open("https://www.netflix.com")
    elif "open calendar" in c.lower():
        webbrowser.open("https://deshgujarat.com")
    elif "open zomato" in c.lower():
        webbrowser.open("https://www.zomato.com")
    elif "open redbus" in c.lower():
        webbrowser.open("https://www.redbus.in")
    elif "open translate" in c.lower():
        webbrowser.open("https://translate.google.co.in/")
    elif "open maps" in c.lower():
        webbrowser.open("https://www.google.com/maps")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open whatsap" in c.lower():
        webbrowser.open("https://whatsapp.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open x" in c.lower():
        webbrowser.open("https://x.com")

    elif c.lower().startswith("play"):     # Play song from music library....
        song = c.lower().replace("play", "").strip()
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():              # Fetch and speak latest news headlines
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey=PUT YOUR API Key")
        if r.status_code == 200:
            
            data = r.json()     # Parse the JSON response                       
            articles = data.get('articles', [])     # Extract the articles
                    
            for article in articles:        # Print the headlines
                speak(article['title'])
    else:
        #If no command matches, send it to AI..
        output = aiProcess(c)
        speak(output) 
         
# Main program execution starts here :
if __name__ == "__main__":
    speak("Initializing Jarvis......")      # Speak startup message
    while True:                    # Run infinite loop to keep listening...
        # Listen for the wake word "Jarvis" &&  obtain audio from the microphone.....
        r = sr.Recognizer()
         
        print("Recognizing......")
        try:                    # Capture wake word from microphone....
            with sr.Microphone() as source:
                print("Listening......")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
                try:            # Convert speech to text
                    word = r.recognize_google(audio)
                except:
                    continue
            if(word.lower() == "jarvis"):    # If wake word is "jarvis"
                speak("Jarvis here.....")

                # Listen for the actual command...
                with sr.Microphone() as source:
                    print("Jarvis Active here...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    # Process the command...
                    processCommand(command)
        # Handle errors safely....
        except Exception as e:
            print("Error; {0}".format(e))