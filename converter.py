from mido import MidiFile
import os


for item in os.listdir('.\midi'):
    mid = MidiFile(f'.\midi\{item}', clip=True)
    print(mid)