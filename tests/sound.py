import os
from pygame import *
import time

#fonction pour transformer le text on son ce qu'on va utiliser pour anoncer
#le nom de l'objet
def textToSound (message):
	os.system('echo "' + message + '" | festival --tts')
	time.sleep(1)
#Son de message de bienvenue
def welcome():
	os.system('echo "' + 'Wellcome i am guessless' + '" | festival --tts')
	time.sleep(1)
#Fonction de son de demarrage
def start ():
	mixer.init()
	mixer.music.load("startSound.MP3")
	mixer.music.play()
	#sound_file=vlc.MediaPlayer("startSound.MP3")
	#sound_file.play()
	time.sleep(10)
#Fonction de son de pulsation lors de la detection de l'objet
def pulsation ():
	mixer.init()
	mixer.music.load("pulsation.mp3")
	mixer.music.play()
	#sound_file=vlc.MediaPlayer("startSound.MP3")
	#sound_file.play()
	time.sleep(10)
#Fonction de son de quit
def Quit ():
	mixer.init()
	mixer.music.load("quitSound.mp3")
	mixer.music.play()
	#sound_file=vlc.MediaPlayer("startSound.MP3")
	#sound_file.play()
	time.sleep(10)
