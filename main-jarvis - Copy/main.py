import random
import openai
import pyttsx3
import speech_recognition as sr
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pyaudio
import wave
import sounddevice as sd
from tkinter import *
import numpy as np
import os
import webbrowser
import pyautogui
import tkinter as tk
import pygame
import os
from PIL import Image, ImageTk
import time
import pyautogui
from threading import Thread
import cv2
import datetime
import time
import requests
import threading


# Example usage

# Set your GPT-3 API key here
openai.api_key = 'Your ChatGpt API key here!'

conversation_closers = ["Anything else you'd like to ask?", "Is there something else I can assist you with?", "Feel free to ask anything else!"]
goodbyes = ["Goodbye!", "Take care!", "See you soon!", "Have a great day!"]

def jarvis_assistant(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=200,
        n=1,
        stop=None,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text.strip()

def speak(text):
    engine = pyttsx3.init()

    # Set the voice (specific to your chosen TTS engine)
    voices = engine.getProperty('voices')
    # Replace the index below with the desired voice index from the voices list
    # For example, 1 corresponds to a different voice than 0
    engine.setProperty('voice', voices[0].id)

    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
        try:
            user_input = recognizer.recognize_google(audio).strip()
            print(f"You: {user_input}")
            return user_input
        except sr.UnknownValueError:
            print("Sorry, I could not understand what you said.")
            return ""
        except sr.RequestError:
            print("Sorry, there was an issue with the speech recognition service.")
            return ""
def speak_async(text):
    def async_speak(text):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.say(text)
        engine.runAndWait()

    threading.Thread(target=async_speak, args=(text,)).start()
def fetch_news(api_key):
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey=13e9671107604f9b8985e48496ab663d"
    response = requests.get(url)
    news_data = response.json()

    if news_data.get('status') == 'ok':
        articles = news_data.get('articles', [])
        return articles
    else:
        print("Error fetching news:", news_data.get('message'))
        return []

class AIAssistant:
    def __init__(self):
        self.active = True

    def start(self):
        print("AI Assistant: Hello! How can I assist you?")
        while self.active:
            command = input("You: ").lower()
            self.handle_command(command)
def display_gif_fullscreen(gif_path):
    # Initialize Pygame
    pygame.init()

    # Get the screen resolution
    screen_info = pygame.display.Info()
    screen_width = screen_info.current_w
    screen_height = screen_info.current_h

    # Set display mode to full screen
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

    # Load the GIF image
    gif = pygame.image.load(gif_path)

    # Calculate the position to center the GIF on the screen
    gif_width = gif.get_width()
    gif_height = gif.get_height()
    x_position = (screen_width - gif_width) // 2
    y_position = (screen_height - gif_height) // 2

    # Create a clock to control frame rate
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with black color
        screen.fill((0, 0, 0))

        # Display the GIF on the screen
        screen.blit(gif, (x_position, y_position))

        # Update the display
        pygame.display.flip()

        # Control the frame rate
        clock.tick(30)  # You can adjust the frame rate as needed
        
    # Quit Pygame when done
    pygame.quit()
class AIAssistant:
    def __init__(self):
        self.active = True


    def set_reminder(self):
        print("AI Assistant: What would you like to be reminded of?")
        reminder_text = recognize_speech()

        if reminder_text:
            print("AI Assistant: When should I remind you? Please specify the time.")
            reminder_time = recognize_speech()

            try:
                reminder_time = datetime.datetime.strptime(reminder_time, '%I:%M %p')
                current_time = datetime.datetime.now().time()

                if reminder_time.time() > current_time:
                    time_difference = (reminder_time - datetime.datetime.now()).seconds
                    print(f"AI Assistant: Reminder set for {reminder_time}.")
                    # Add your reminder notification code here, such as sending a notification or alert.
                else:
                    print("AI Assistant: The specified time has already passed.")
            except ValueError:
                print("AI Assistant: Sorry, I couldn't understand the time.")

# Call the function and pass the path to your GIF file
gif_path = "jarvis_orb.gif"
def display_gif_thread(gif_path):
    display_gif_fullscreen(gif_path)
display_gif_fullscreen(gif_path)

def create_file(file_name, content=""):
    try:
        with open(file_name, "w") as file:
            file.write(content)
        print(f"Jarvis: File '{file_name}' created successfully.")
    except Exception as e:
        print("Jarvis:", e)
def get_current_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%I:%M %p")
    return current_time

def handle_command(self, command):
    if "log of" in command:
        self.go_to_sleep()
    elif command == "go":
        print("AI Assistant: Going offline.")
        self.active = False
    elif command == "quit":
        print("AI Assistant: Quitting.")
        self.active = False
    elif command == "you can go":
        self.active = False    
    elif command.startswith("create file"):
        parts = command.split()
        if len(parts) > 2:
            file_name = " ".join(parts[2:])
            print(f"AI Assistant: Do you want to create a file named '{file_name}'? (yes/no)")
            confirmation = input("You: ").lower()
            if confirmation == "yes":
                create_file(file_name)
            else:
                print("AI Assistant: File creation canceled.")
        else:
            print("AI Assistant: Please provide a valid file name.")
    else:
        print("AI Assistant: I'm here to help!")


    def go_to_sleep(self):
        print("AI Assistant: Going to sleep.")
        while True:
            wakeup_command = input("You: ").lower()
            if wakeup_command == "wake up":
                print("AI Assistant: Waking up.")    

def send_email(subject, recipient, content):
    smtp_server = "smtp.elasticemail.com"
    smtp_port = 2525
    smtp_username = "moxiyay289@chodyi.com"
    smtp_password = "B4B47E93A941C9E0C4D11CCB463269C92D3D"

    msg = MIMEMultipart()
    msg["From"] = smtp_username
    msg["To"] = recipient
    msg["Subject"] = subject
    msg.attach(MIMEText(content, "plain"))

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, recipient, msg.as_string())
def the_task_automation():
    pyautogui.moveTo(169, 752,2)
    pyautogui.click()
    pyautogui.write("Notepad")
    pyautogui.press("Enter")
    
def record_audio(filename, duration=5):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100

    audio = pyaudio.PyAudio()

    stream = audio.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

    frames = []
    for i in range(0, int(RATE / CHUNK * duration)):
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    audio.terminate()

    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

def play_audio(filename):
    wf = wave.open(filename, 'rb')
    data = wf.readframes(wf.getnframes())
    data = np.frombuffer(data, dtype=np.int16)

    sd.play(data, samplerate=wf.getframerate())
    sd.wait()

def open_application(application_name):
    try:
        os.system(application_name)
    except Exception as e:
        print("Jarvis:", e)        
    
def open_file(file_path):
    try:
        os.startfile(file_path)
    except Exception as e:
        print("Jarvis:", e)
def open_webcam():
    # Open the webcam
    cap = cv2.VideoCapture(0)

    while True:
        # Capture a frame from the webcam
        ret, frame = cap.read()

        # Display the captured frame
        cv2.imshow("Webcam", frame)

        # Exit loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close all windows
    cap.release()
    cv2.destroyAllWindows()        
def main_thread():
    main()
    
def open_website(website_url):
    try:
        webbrowser.open(website_url)
    except Exception as e:
        print("Jarvis:", e)

# enable this if you want a cam scanner

# def detect_faces():
#     cap = cv2.VideoCapture(0)
#     face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break
        
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
#         for (x, y, w, h) in faces:
#             cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
#         cv2.imshow("Face Detection", frame)
        
#         if len(faces) > 0:
#             cap.release()
#             cv2.destroyAllWindows()
#             return True
        
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
    
#     cap.release()
#     cv2.destroyAllWindows()
#     return False

def main():
    # if detect_faces():
    #     print("Analyzing face...")
    #     time.sleep(3)  # Delay for approximately 3 seconds
        
        # Start AI assistant
        print("Analyzing AI...")
        time.sleep(2) # Delay for approximately
        while True:
            user_input = recognize_speech()

            if any(phrase in user_input.lower() for phrase in ["exit", "quit", "bye", "you can go", "log off", "Allah Hafiz"]):
                print("Jarvis: Goodbye!")
                break

            elif "open" in user_input.lower():
                parts = user_input.lower().split()
                keyword_index = parts.index("open")
                if keyword_index + 1 < len(parts):
                    target = parts[keyword_index + 1]

                    if target == "notepad":
                        open_application("notepad.exe")
                    elif target == "whats the time" or "time kya hai" or "can you tell me the time" or "what is the time right now" or "what is the time rightnow":
                        get_current_time()
                     
                    elif target == "calculator":
                        open_application("calc.exe")
                    elif target == "browser":
                        open_application("chrome.exe")
                    elif target == "webcam" or "webcam khol" or "webcam khloien" or "webcam khloin":
                        open_application(open_webcam)
                        
                    elif target == "paint":
                        open_application("mspaint.exe")# Change this to your preferred browser
                    elif target == "file":
                        
                        
                        if keyword_index + 2 < len(parts):
                            file_path = " ".join(parts[keyword_index + 2:])
                            open_file(file_path)
                        else:
                            print("Jarvis: Please provide a valid file path.")
                    elif target == "website":
                        if keyword_index + 2 < len(parts):
                            website_url = parts[keyword_index + 2]
                            open_website(website_url)
                        else:
                            print("Jarvis: Please provide a valid website URL.")
                    else:
                        print("Jarvis: I don't know how to open that.")
                        if target == "search":
                            if keyword_index + 2 < len(parts):
                                search_query = " ".join(parts[keyword_index + 2:])
                                search_url = f"https://www.google.com/search?q={search_query}"
                                open_website(search_url)
                            else:
                                print("Jarvis: Please provide a valid search query.")
                    
            elif user_input.lower().startswith("send email"):
                subject = input("Jarvis: What's the subject of the email? ")
                recipient = input("Jarvis: Who is the recipient? ")
                content = input("Jarvis: What's the content of the email? ")
                send_email(subject, recipient, content)
                print("Jarvis: Email sent successfully!")

            elif user_input.lower().startswith("record audio"):
                duration = int(input("Jarvis: How many seconds do you want to record? "))
                filename = "recorded_audio.wav"
                record_audio(filename, duration)
                print("Recording...")
                print(f"Jarvis: Audio recorded and saved as '{filename}'")

            else:
                prompt = f"You: {user_input}\nJarvis:"
                response = jarvis_assistant(prompt)
                print("Jarvis:", response)
                speak(response)
                print("Jarvis:", random.choice(conversation_closers))
if __name__ == "__main__":
  def main_thread():
    main()

if __name__ == "__main__":
    voice_thread = threading.Thread(target=speak_async, args=("Hello my name is jarvis",))
    gif_thread = threading.Thread(target=display_gif_thread, args=("jarvis_orb.gif",))
    main_thread = threading.Thread(target=main_thread)
    voice_thread.start()
    gif_thread.start()
    main_thread.start()