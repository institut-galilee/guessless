import os

where_path = "cd /home/pi/Documents/rpi-rgb-led-matrix/"
params = " --led-rows=32 --led-cols=64 --led-no-hardware-pulse"
params_py = " --led-rows 32 --led-cols 64 --led-no-hardware-pulse NO_HARDWARE_PULSE"

def start() :
    os.system(where_path + "utils && sudo ./video-viewer logo.webm" + params)

def guess() :
    #os.system(where_path + "bindings/python/samples && sudo python ./pulsing-brightness.py " + params_py)
    os.system(where_path + "utils && sudo ./video-viewer guess.webm" + params)

def bye() :
    os.system(where_path + "utils && sudo ./video-viewer bye.webm" + params)
