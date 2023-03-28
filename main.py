from datetime import datetime
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from playwright.sync_api import sync_playwright
import time

now = str

def adjust_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevel(1, None)

def start_alarm(playwright):
    adjust_volume()

    chromium = playwright.chromium
    browser = chromium.launch(headless= False)
    page = browser.new_page()
    page.goto(url= 'https://www.youtube.com/watch?v=uWBo10vVxwo/',
        wait_until= 'domcontentloaded')
    time.sleep(1)
    page.locator("video").click(click_count= 2, delay= 0.7)
    time.sleep(3*60)
    browser.close()

print("Selecione a hora em que deseja que o alarme toque (Ex. 06:30)")
userInput = input(">> ")
while True:
    now = datetime.now()

    if now.strftime("%H:%M") == userInput:
        with sync_playwright() as playwright:
            start_alarm(playwright)
        break