import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import threading
from tkinter import *
from PIL import ImageTk, Image

class AssistanceGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Assistant")
        self.root.geometry('600x600')

        # Background Image
        try:
            self.bg = ImageTk.PhotoImage(Image.open("images/background.png"))
            bg_label = Label(self.root, image=self.bg)
            bg_label.place(x=0, y=0)
        except Exception as e:
            print("Background image error:", e)

        # Frame Image
        try:
            self.centre = ImageTk.PhotoImage(Image.open("images/frame_image.jpg"))
            centre_label = Label(self.root, image=self.centre)
            centre_label.place(x=100, y=100, width=400, height=400)
        except Exception as e:
            print("Frame image error:", e)

        Button(self.root, text='START', font=("Times New Roman", 14), command=self.start_thread).place(x=150, y=520)
        Button(self.root, text='CLOSE', font=("Times New Roman", 14), command=self.close_window).place(x=350, y=520)

    def start_thread(self):
        # Launch voice assistant loop in a separate thread
        threading.Thread(target=self.start_option).start()

    def start_option(self):
        listener = sr.Recognizer()
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)

        def speak(text):
            print("Assistant:", text)
            engine.say(text)
            engine.runAndWait()

        def start():
            hour = datetime.datetime.now().hour
            if 0 <= hour < 12:
                wish = "Good Morning!"
            elif 12 <= hour < 18:
                wish = "Good Afternoon!"
            else:
                wish = "Good Evening!"
            speak(f"Hello, {wish} I am your voice assistant. Please tell me how may I help you")

        def take_command():
            try:
                with sr.Microphone() as source:
                    print("Listening...")
                    listener.adjust_for_ambient_noise(source)
                    voice = listener.listen(source, timeout=5)
                    instruction = listener.recognize_google(voice)
                    return instruction.lower()
            except sr.WaitTimeoutError:
                print("No voice input detected.")
                return ""
            except Exception as e:
                print("Error taking command:", e)
                return ""

        def run_command():
            instruction = take_command()
            if instruction:
                print("You said:", instruction)
            else:
                speak("I couldn’t catch that, please try again.")
                return True

            if 'who are you' in instruction:
                speak('I am your personal voice assistant')

            elif 'what can you do for me' in instruction:
                speak('I can play songs, tell time, and help you browse websites or Wikipedia')

            elif 'current time' in instruction:
                time_now = datetime.datetime.now().strftime('%I:%M %p')
                speak('Current time is ' + time_now)

            elif 'open' in instruction:
                websites = {
                    'google': 'https://www.google.com',
                    'youtube': 'https://www.youtube.com',
                    'facebook': 'https://www.facebook.com',
                    'python geeks': 'https://pythongeeks.org',
                    'linkedin': 'https://www.linkedin.com',
                    'gmail': 'https://mail.google.com',
                    'stack overflow': 'https://stackoverflow.com'
                }
                for key, url in websites.items():
                    if key in instruction:
                        speak(f'Opening {key}')
                        webbrowser.open(url)
                        break
                else:
                    speak('Website not recognized')

            elif 'shutdown' in instruction:
                speak('I am shutting down')
                self.close_window()
                return False

            else:
                speak('I did not understand, can you repeat again')

            return True

        start()
        while True:
            if not run_command():
                break

    def close_window(self):
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = AssistanceGUI(root)
    root.mainloop()