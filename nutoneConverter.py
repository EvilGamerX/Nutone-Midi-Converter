from mido import MidiFile
import os

def nutoneConvert(overwrite):
    if not os.path.exists('nutone'):
        os.makedirs('nutone')
        print('Nutone directory created. Please add files to that directory and try again.')
        return
    print(f'Nutone Converter. Overwrite {overwrite}')