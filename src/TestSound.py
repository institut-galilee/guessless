import os
import time

message = 'Bonjour la team Guessless.'

print('Ceci est une demonstration')
os.system('echo "' + 'Ceci est une demonstration' + '" | festival --tts')
time.sleep(1)
os.system('echo "' + message + '" | festival --tts')
time.sleep(1)