#import pygame as p
import speech_recognition as sr
# from pydub import AudioSegment
# from pydub.playback import _play_with_simpleaudio as play
import os
# Add ffmpeg to PATH before importing pydub
os.environ["PATH"] += os.pathsep + r"C:\ffmpeg\bin"

from pydub import AudioSegment
from pydub.playback import play

recognizer = sr.Recognizer()


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

with sr.Microphone() as source:
    print("listening..")

    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio).lower()
        print(text)
        audio_to_play = None

        for title, audio_file in audio_files.items():
            if title in text:
                print("audio found, playing!")
                audio_to_play = AudioSegment.from_mp3(audio_file)
                break
        
        if audio_to_play:
            play(audio_to_play)
            print("playing")
        else:
            print("couldn't find matching audio")

    except Exception as e:
        print("something went wrong! Error:", e)



