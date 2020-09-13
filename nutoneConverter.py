from mido import MidiFile
import os
import json

def nutoneConvert(overwrite):
    if not os.path.exists('nutone'):
        os.makedirs('nutone')
        print('Nutone directory created. Please add files to that directory and try again.')
        return
    if not os.path.exists('converted/midi'):
    with open('nutoneNotes.json') as f:
        conversionTable = json.load(f)
    print(conversionTable)
    for item in os.listdir('nutone'):
        print(item)