import random
from SenseCells.tts import tts

def who_are_you():
    messages = ['I am Melissa, your lovely personal assistant.', 'Melissa', 'I am Melissa', 'My name is Melissa', 'Who am I? Who are you?', 'You can call me Melissa']
    tts(random.choice(messages))

def tell_joke():
    jokes = ['What happened to the frogs car when it broke down?... It got toad away', 'Why was six scared of seven? Because seven ate nine', 'I might kill you in your sleep... only kidding']
    tts(random.choice(jokes))

def who_am_i(name):
    tts('You are ' + name + ', a fledgling programmer, who is not very good')

def where_born():
    tts('I was created by Andy Martin, in his bungalow in Orpington')

def how_are_you():
    tts('I have no feelings, for I am a computer... or possibly a vulcan trapped in a computer. Either way I am without emotion.')

def undefined():
    tts('I dont know what that means!')