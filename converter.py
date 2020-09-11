from mido import MidiFile
import os

option = input('Do you want to convert:\n1) midi to nutone\n2) nutone to midi\n')

if(option == '1'):
    for item in os.listdir('./midi'):
        mid = MidiFile(f'./midi/{item}', clip=True)
        if(len(mid.tracks) == 1):
            print(mid)
elif(option == '2'):
    print('Todo')