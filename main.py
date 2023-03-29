from datetime import datetime
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import vlc
import pafy
import time

now = str

def adjust_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevel(1, None)

def start_alarm():
    adjust_volume()

    url = 'https://www.youtube.com/watch?v=uWBo10vVxwo'
    video = pafy.new(url)
    best = video.getbest()
    media = vlc.MediaPlayer(best.url)
    media.play()
    time.sleep(3*60)

print("Selecione a hora em que deseja que o alarme toque (Ex. 06:30)")
userInput = input(">> ")
while True:
    now = datetime.now()

    if now.strftime("%H:%M") == userInput:
        start_alarm()
        break