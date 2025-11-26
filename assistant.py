# -------------------------------
# Import Required Modules
# -------------------------------
import os                          # open system apps (notepad, calculator, etc.)
import datetime                    # fetch current time/date
import pyttsx3                     # text-to-speech engine
import speech_recognition as sr    # speech-to-text (voice commands)
import webbrowser                  # open websites in browser
import wikipedia                   # fetch Wikipedia summaries
import pyjokes                     # for jokes
import pywhatkit                   # for WhatsApp messages & YouTube searches
import psutil                      # for battery status
import pyautogui                   # for screenshots

# -------------------------------
# Create Engine for Text-to-Speech
# -------------------------------
engine = pyttsx3.init()
engine.setProperty("rate", 105)   # speed of speech

# Speak function → speaks + prints text
def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# -------------------------------
# Take Voice Command Function
# -------------------------------
def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Vintunna ....Chepuuu..!")
        audio = listener.listen(source)

        try:
            command = listener.recognize_google(audio)  # convert speech → text
            command = command.lower()
            print("You said:", command)
            return command
        except:
            return ""

# -------------------------------
# Main Assistant Logic
# -------------------------------
def run_assistant():
    command = take_command()

    # 1. Time
    if "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {time}")

    # 2. Date
    elif "date" in command:
        today = datetime.date.today()
        speak(f"Today's date is {today}")

    # 3. Open Notepad
    elif "open notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")

    # 4. Open YouTube
    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com/")

    # 5. Wikipedia Search
    elif "tell me about" in command or "who is" in command or "what is" in command:
        try:
            topic = command.replace("tell me about", "").replace("who is", "").replace("what is", "").strip()
            if topic:
                info = wikipedia.summary(topic, sentences=2)
                speak(info)
            else:
                speak("Please say the topic again.")
        except Exception:
            speak("Sorry, I could not find information about that.")

    # 6. Google Search
    elif "search" in command:
        query = command.replace("search", "").strip()
        speak(f"Searching Google for {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")

    # 7. Open Google directly
    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    # 8. Play Song on YouTube
    elif "play song" in command:
        speak("Playing a song on YouTube")
        pywhatkit.playonyt("top songs")

    # 9. Tell a Joke
    elif "joke" in command:
        joke = pyjokes.get_joke()
        speak(joke)

    # 10. Open Calculator
    elif "open calculator" in command:
        speak("Opening Calculator")
        os.system("calc")

    # 11. Search Location on Google Maps
    elif "where is" in command:
        location = command.replace("where is", "").strip()
        if location:
            speak(f"Showing {location} on Google Maps")
            webbrowser.open(f"https://www.google.com/maps/place/{location}")

    # 12. Send WhatsApp Message
    elif "send message" in command:
        speak("Enter number and message manually for now.")
        number = input("Enter phone number with country code (e.g., +919876543210): ")
        message = input("Enter your message: ")
        pywhatkit.sendwhatmsg_instantly(number, message)
        speak("Message sent!")

    # 13. Battery Status
    elif "battery" in command:
        battery = psutil.sensors_battery()
        percent = battery.percent
        speak(f"Battery is at {percent} percent")

    # 14. Take Screenshot
    elif "screenshot" in command:
        img = pyautogui.screenshot()
        img.save("screenshot.png")
        speak("Screenshot taken and saved as screenshot.png")

    # 15. Lock PC
    elif "lock" in command:
        speak("Locking your computer")
        os.system("rundll32.exe user32.dll, LockWorkStation")

    # 16. Shutdown
    elif "shutdown" in command:
        speak("Shutting down your computer")
        os.system("shutdown /s /t 1")

    # 17. Restart
    elif "restart" in command:
        speak("Restarting your computer")
        os.system("shutdown /r /t 1")

    # Exit
    elif "bye" in command or "stop" in command:
        speak("UNTA ...Byee ra BITTUU")
        exit()

    # Fallback
    else:
        speak("Shhh..Abbaa,,,sarigga cheppu!! ledante chasthav na chetilo..")

# -------------------------------
# Main Program Loop
# -------------------------------
if __name__ == "__main__":
    speak("HEYY ...NAMASTSTE  ..NENU ME ALEXAAABABY")
    while True:
        run_assistant()


