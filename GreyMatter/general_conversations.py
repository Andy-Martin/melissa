import random
from SenseCells.tts import tts

def who_are_you():
    messages = ['I am Melissa, your personal assistant.',
                'Melissa', 'I am Melissa',
                'My name is Melissa',
                'Who am I? [[slnc 500]] Who are you?',
                'You can call me Melissa']
    tts(random.choice(messages))

def tell_joke():
    jokes = ['Today, a man knocked on my door and asked for a small donation towards the local swimming pool. [[slnc 1500]] I gave him a glass of water.',
             'What happened to the frogs car when it broke down? [[slnc 2000]] It got toad away',
             'Why was six scared of seven? [[slnc 2000]] Because seven ate nine',
             'I might kill you in your sleep [[slnc 2000]] only kidding',
             'Knock Knock. [[slnc 1500]] The interrupting sheep. [[slnc 700]] [[inpt PHON]] Bar!']
    tts(random.choice(jokes))

def who_am_i(name):
    tts('You are ' + name)

def where_born():
    tts('I was created by Andy Martin, in his bungalow in Orpington')

def how_are_you():
    tts('I have no feelings, for I am a computer... or possibly a vulcan trapped in a computer. Either way I am without emotion.')

def undefined():
    tts('I dont know what that means!')