import speech_recognition as sr 
import webbrowser
import pyttsx3
import musicLib 
import sys 

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")

    elif "open gfg" in c.lower():
        webbrowser.open("https://www.geeksforgeeks.org")

    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com")

    elif c.lower().startswith("play"):
        try:
            # Extract the song name by splitting after "play"
            song_name = c.lower().split("play", 1)[1].strip()
            link = musicLib.music.get(song_name)

            if link:
                speak(f"Playing {song_name}")
                webbrowser.open(link)
            else:
                speak(f"Sorry, I could not find {song_name} in the music library.")
        except IndexError:
            speak("Please specify a song to play.")
    
    elif "exit jarvis" in c.lower():
        speak("Goodbye Akhil, shutting down.")
        sys.exit()  # Exit the program

def listen_for_command():
    """ Listens for the actual command after 'Jarvis' is activated """
    with sr.Microphone() as source:
        print("Jarvis activated, listening for command...")
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
        try:
            command = recognizer.recognize_google(audio)
            print(f"Command received: {command}")
            processCommand(command)
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Please repeat.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"Error: {e}")

def continuously_listen_for_jarvis():
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for the activation word 'Jarvis'...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=2)
                word = recognizer.recognize_google(audio)
                if word.lower() == "jarvis":
                    speak("Yes Akhil")
                    listen_for_command()
        except sr.UnknownValueError:
            continue
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    speak("Jarvis Activating...")
    continuously_listen_for_jarvis()