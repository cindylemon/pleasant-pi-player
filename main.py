import pygame as p
import speech_recognition as sr

recognizer = sr.Recognizer()

p.mixer.init()

with sr.Microphone() as source:
    print("listening..")

    recognizer.adjust_for_ambient_noise(source)
    input = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(input)
        print(text)

    except Exception as e:
        print("something went wrong! Error:", e)



