import os
import time


def textToSound (message):
	os.system('echo "' + message + '" | festival --tts')
	time.sleep(1)

def welcomeBro():
	os.system('echo "' + 'Bienvenu Je suis Guessless' + '" | festival --tts')
	time.sleep(1)