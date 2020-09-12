from midiConverter import midiConvert
from nutoneConverter import nutoneConvert

option = input('Do you want to convert:\n1) midi to nutone\n2) nutone to midi\n')

overwrite = input('Do you overwrite existing conversions: [Y]es, [N]o\n')

if(option == '1'):
    midiConvert(not overwrite.isspace() and overwrite[0].lower() == 'y')
elif(option == '2'):
    nutoneConvert(not overwrite.isspace() and overwrite[0].lower() == 'y')