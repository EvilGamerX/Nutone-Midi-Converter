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
        textFile = open(f'nutone/{item}', 'r').read().split(', ')
        item = item.split('.')[0]          
        mid = MidiFile()
        track = MidiTrack()
        mid.tracks.append(track)
        print(f'Converting file: {item}')
        program = 18
        programInput = input('Please enter the number of midi instrument you would like to generate with.\n')
        try:
            program = int(programInput)
        except ValueError:
            print(f'Not a number, defaulting to program {program}')
        if( program > 128):
            print(f'Number too large, defaulting to program 18')
            program = 18
        track.append(Message('program_change', program=program, time=0))

        speed = 1920
        speedInput = input('Please select the speed of the Nutone song (invalid input will default to Medium):\n1) Slow\n2) Medium\n3) Fast\n')

        if(speedInput == '1'):
            speed *= 2
        elif(speedInput == '3'):
            speed /= 2

        for note in textFile:
            if(note == '00'):
                break
            midiNote = rootNote
            noteLenth = 0.125
            if(note[0] == conversionTable['octaveKey']):
                midiNote += 12
                note = note[1:]
            midiNote +=  int(note[0], 12)
            noteLenth *= noteMultipliers[int(note[1])-1] * speed
            track.append(Message('note_on', note=midiNote, velocity=127, time=0))
            track.append(Message('note_off', note=midiNote, velocity=127, time=int(noteLenth)))
        
        mid.save(f'converted/midi/{item}.mid')


            
