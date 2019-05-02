import os
import time

message = 'Hello Régis, uou are a motherfucker'

print('Ceci est une demonstration')
#os.system('echo "' + 'Hello motherfucker' + '" | festival --tts')
time.sleep(1)
os.system('echo "' + message + '" | festival --tts')
time.sleep(1)
