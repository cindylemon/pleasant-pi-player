import pygame as p
import speech_recognition as sr
import os
import pvporcupine
from pvrecorder import PvRecorder

# Add ffmpeg to PATH before importing pydub
os.environ["PATH"] += os.pathsep + r"C:\ffmpeg\bin"

from pydub import AudioSegment
from pydub.playback import play

recognizer = sr.Recognizer()
p.mixer.init()


audio_files = {
    "art of war 2":"audio/art_of_war_chinese_1506_librivox/artofwartwo.mp3",
    "art of war 3":"audio/art_of_war_chinese_1506_librivox/artofwar_03_sun_64kb.mp3",
    "art of war 4":"audio/art_of_war_chinese_1506_librivox/artofwar_04_sun_64kb.mp3",
    "art of war 5":"audio/art_of_war_chinese_1506_librivox/artofwar_05_sun_64kb.mp3",
    "art of war 6":"audio/art_of_war_chinese_1506_librivox/artofwar_06_sun_64kb.mp3",
    "art of war 7":"audio/art_of_war_chinese_1506_librivox/artofwar_07_sun_64kb.mp3",
    "art of war 8":"audio/art_of_war_chinese_1506_librivox/artofwar_08_sun_64kb.mp3",
    "art of war 9":"audio/art_of_war_chinese_1506_librivox/artofwar_09_sun_64kb.mp3",
    "art of war 10":"audio/art_of_war_chinese_1506_librivox/artofwar_10_sun_64kb.mp3",
    "art of war 11":"audio/art_of_war_chinese_1506_librivox/artofwar_11_sun_64kb.mp3",
    "art of war 12":"audio/art_of_war_chinese_1506_librivox/artofwar_12_sun_64kb.mp3",
    "art of war 13":"audio/art_of_war_chinese_1506_librivox/artofwar_13_sun_64kb.mp3"
}

keywords=["bumblebee", "jarvis"]

porcupine = pvporcupine.create(
        access_key="REMOVED_API_KEY",
        keywords = keywords)
recorder = PvRecorder(device_index=-1, frame_length=porcupine.frame_length)




def wakeWord():
    print("running")
    try:
        recorder.start()
        print("porcupine started")
        while True:
            keyword_index = porcupine.process(recorder.read())
            if keyword_index >= 0:
                print(f"deteced {keywords[keyword_index]}")
                break
        
    except KeyboardInterrupt:
        recorder.stop()
    finally:
        porcupine.delete()
        recorder.delete()




def audioSearch():
    while True:
        wakeWord()
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            print("listening..")

            try:
                text = recognizer.recognize_google(audio).lower()
                print(text)
                if "exit" in text:
                    print("exiting application")
                    break
                audio_to_play = None

                for title, audio_file in audio_files.items():
                    if title in text:
                        print("audio found, playing!")
                        p.mixer.music.load(audio_to_play)
                        break
                
                if audio_to_play:
                    print("playing")
                    p.mixer.music.play()
                else:
                    print("couldn't find matching audio")

            except Exception as e:
                print("something went wrong! Error:", e)

print("hello?")
audioSearch()



