import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to make the assistant speak
def talk(text):
    engine.say(text)
    engine.runAndWait()

# Function to take voice commands
def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            voice = recognizer.listen(source)
            command = recognizer.recognize_google(voice)
            command = command.lower()
            print(f"User said: {command}")
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return "None"
    except sr.RequestError:
        print("Sorry, my speech service is down.")
        return "None"
    except Exception as e:
        print(f"Error: {e}")
        return "None"
    return command

# Function to run the voice assistant
def run_assistant():
    command = take_command()
    if command == "None":
        return
    talk(f"You said: {command}")

if __name__ == "__main__":
    while True:
        run_assistant()
