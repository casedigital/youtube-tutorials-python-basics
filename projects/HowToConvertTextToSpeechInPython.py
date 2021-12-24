# How To Convert Text To Speech In Python?
# https://youtu.be/edNNM7f-8XM

import pyttsx3
import time
import os


def test_different_voices(test_str, num_voices, speech_engine):
    voices = speech_engine.getProperty('voices') 
    idx_found = -1
    if num_voices > len(voices):
        num_voices = len(voices)

    for idx, voice in enumerate(voices[:num_voices]):
        speech_engine.setProperty('voice', voice.id)
        cur_voice = [val for val in speech_engine.getProperty("voices") if val.id == voice.id][0]
        voice_welcome = f'I my name is {cur_voice.name} '
        engine.say(voice_welcome + test_str)


if __name__ == '__main__':
    engine = pyttsx3.init()
    saying = f'I just wanted to say you should subscribe to Case Digital!'
    engine.say(saying)

    engine.say('Now I am going to test out some different voices!')
    engine.say('3')
    engine.say('2')
    engine.say('1')
    engine.say('Go')
    time.sleep(1)
    engine.runAndWait()

    test_different_voices(saying, 10, engine)
    engine.runAndWait()
