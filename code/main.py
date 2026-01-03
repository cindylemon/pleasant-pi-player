import pygame as p
import speech_recognition as sr
import os
import pvporcupine
from pvrecorder import PvRecorder
from dotenv import load_dotenv

from pydub import AudioSegment
from pydub.playback import play

#print("imported")

#for index, name in enumerate(sr.Microphone.list_microphone_names()):
#    print(f"{index}: {name}")
#mic = sr.Microphone(device_index = 2)

class PiPlayer:
    r = sr.Recognizer()
    def __init__(self):
        self.recognizer = sr.Recognizer()
        p.mixer.init()
        
        
        self.audio_library = self.get_default_library()
        
        self.listening = True
        self.current_track = None
        self.volume = 0.7
        p.mixer.music.set_volume(self.volume)
        
        
        self.keywords=["bumblebee", "jarvis"]
        self.key = os.getenv('PORCUPINE_KEY')
        print(key)

        porcupine = pvporcupine.create(
                access_key=key,
                keywords = self.keywords)

        self.recorder = PvRecorder(device_index=2, frame_length=porcupine.frame_length)

        print("voice assistant initialized")
        print(f"wake words: "{','.join(self.keyworkds)}")

        p.mixer.init()


    def getDefaultAudio(self):
        return { = {
            "art of war": {
                "chapters": {
                    "2":"audio/art_of_war_chinese_1506_librivox/artofwartwo.mp3",
                    "3":"audio/art_of_war_chinese_1506_librivox/artofwar_03_sun_64kb.mp3",
                    "4":"audio/art_of_war_chinese_1506_librivox/artofwar_04_sun_64kb.mp3",
                    "5":"audio/art_of_war_chinese_1506_librivox/artofwar_05_sun_64kb.mp3",
                    "6":"audio/art_of_war_chinese_1506_librivox/artofwar_06_sun_64kb.mp3",
                    "7":"audio/art_of_war_chinese_1506_librivox/artofwar_07_sun_64kb.mp3",
                    "8":"audio/art_of_war_chinese_1506_librivox/artofwar_08_sun_64kb.mp3",
                    "9":"audio/art_of_war_chinese_1506_librivox/artofwar_09_sun_64kb.mp3",
                    "10":"audio/art_of_war_chinese_1506_librivox/artofwar_10_sun_64kb.mp3",
                    "11":"audio/art_of_war_chinese_1506_librivox/artofwar_11_sun_64kb.mp3",
                    "12":"audio/art_of_war_chinese_1506_librivox/artofwar_12_sun_64kb.mp3",
                    "13":"audio/art_of_war_chinese_1506_librivox/artofwar_13_sun_64kb.mp3"
            }}}
        }

    load_dotenv()

    def speak(self, text):
        print(f"{text}")
        #use os to speak the text


    def wakeWord(self):
        print("waiting for wake word")
        try:
            if not self.recorder.is_recording:
                self.recorder.start()
                
            print("porcupine started")
            
            while self.listening:
                pcm = self.recorder.read()
                keyword_index = porcupine.process(recorder.read())
                
                if keyword_index >= 0:
                    print(f"deteced {keywords[keyword_index]}")
                    os.system("speaker-test -t sine -f 1000 -l 1 -p 100000 >/dev/null 2>&1 &")
                    return True
            
        except Exception as e:
            print(e)
            recorder.stop()
            return False

    def listen(self):
        with sr.Microphone() as source:
        self.recognizer.adjust_for_ambient_noise(source, duration = 0.5)
                
        print("listening..")
        
         try:
            audio = self.recognizer.listen(source, timeout = 5, phrase_time_limit = 15)
            text = recognizer.recognize_google(audio).lower()
            print(f"heard: '{text}'")
            return text
        except sr.WaitTimeoutError:
            print("no command heard")
            return None
        except sr.UnknownValueError:
            print("could not understand")
            return None
        except Exception as e:
            print(e)
            return None


    def audioSearch():
        while True:
            wakeWord()
            

                    audio_to_play = None

                    for title, audio_file in audio_files.items():
                        if title in text:
                            print("audio found, playing!")
                            audio_to_play = audio_file
                            p.mixer.music.load(audio_to_play)
                            break
                    
                    if audio_to_play:
                        print("playing")
                        p.mixer.music.play()
                    else:
                        print("couldn't find matching audio")
                
                except KeyboardInterrupt:
                    print("user interuppted operation")

                except Exception as e:
                    print("something went wrong! Error:", e)
                    

print("hello?")
audioSearch()
# if recorder.is_recording:
#     recorder.stop()
#     porcupine.delete()
#     recorder.delete()


