import os
import time
from pygame import *


def textToSound (message):
	os.system('echo "' + message + '" | festival --tts')
	time.sleep(1)

def welcomeBro():
	os.system('echo "' + 'Wellcome i am guessless' + '" | festival --tts')
	time.sleep(1)

def start ():
	mixer.init()
	mixer.music.load("startSound.MP3")
	mixer.music.play()
	#sound_file=vlc.MediaPlayer("startSound.MP3")
	#sound_file.play()
	time.sleep(10)	
