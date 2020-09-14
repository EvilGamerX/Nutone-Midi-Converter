from mido import MidiFile, MidiTrack, Message
import os
import json

rootNote = 48
noteMultipliers = [1, 2, 3, 4, 6, 8]

def nutoneConvert(overwrite):
    if not os.path.exists('nutone'):
        os.makedirs('nutone')
        print('Nutone directory created. Please add files to that directory and try again.')
        return
    if not os.path.exists('converted/midi'):
        os.makedirs('converted/midi')
        print('Converted midi directory created.')
    with open('nutoneNotes.json') as f:
        conversionTable = json.load(f)
    for item in os.listdir('nutone'):
        print(item)
        textFile = open(f'nutone/{item}', 'r').read().split(', ')
        item = item.split('.')[0]
        print(textFile)            
        mid = MidiFile()
        track = MidiTrack()
        mid.tracks.append(track)
        track.append(Message('program_change', program=12, time=0))


        for note in textFile:
            if(note == '00'):
                break
            midiNote = rootNote
            noteLenth = 0.125
            if(note[0] == conversionTable['octaveKey']):
                midiNote += 12
                note = note[1:]
            midiNote +=  int(note[0], 12)
            noteLenth *= int(note[1]) * 1000
            print(f'{midiNote} | {noteLenth}\n')
            track.append(Message('note_on', note=midiNote, velocity=64, time=int(noteLenth)))
            track.append(Message('note_off', note=midiNote, velocity=127, time=int(noteLenth)))
        
        mid.save(f'converted/midi/{item}.mid')


            
