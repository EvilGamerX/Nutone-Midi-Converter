from mido import MidiFile
import os

def midiConvert(overwrite):
    if not os.path.exists('midi'):
        os.makedirs('midi')
        print('midi directory created. Please add files to that directory and try again.')
        return
    for item in os.listdir('midi'):
        mid = MidiFile(f'./midi/{item}', clip=True)
        if(len(mid.tracks) == 1):
            print(mid)