import speech_recognition as sr
import yaml

from GreyMatter.SenseCells.tts import tts
from brain import brain

from GreyMatter import play_music

profile = open('profile.yaml')
profile_data = yaml.safe_load(profile)
profile.close()

# Functioning Variables
name = profile_data['name']
city_name = profile_data['city_name']
city_code = profile_data['city_code']
speech_text = ""
music_path = profile_data['music_path']

tts('Welcome' + name + '. How can I help you?')

play_music.mp3gen(music_path)


def main():
    global speech_text
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    try:
        speech_text = r.recognize_google(audio).lower().replace("'", "")
        print("Melissa thinks you said '" + speech_text + "'")
    except sr.UnknownValueError:
        print("Melissa could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    brain(name, speech_text, city_name, city_code)


main()
