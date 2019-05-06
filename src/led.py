where_path = "cd /home/pi/Documents/rpi-rgb-led-matrix/utils/ && "
params = " --led-rows=32 --led-cols=64 --led-no-hardware-pulse"

def start() :
    os.system(where_path + "sudo ./video-viewer videoLogo.webm" + params)

def guess() :
    os.system(where_path + "sudo ./video-viewer guess.webm" + params)
