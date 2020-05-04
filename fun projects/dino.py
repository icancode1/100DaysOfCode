import pyautogui
from PIL import ImageGrab, Image
# import numpy
# from numpy import asarray
import time


def hitKeyOnKeyBoard(key):
    pyautogui.keyDown(key)


def isCollide(data):
    for i in (300, 415):
        for j in (588, 702):
            if data[i, j] < 100:
                hitKeyOnKeyBoard("up")
                return True
    


if __name__ == "__main__":
    print("Dino game bot is about to start in 3 seconds")
    time.sleep(3)
    hitKeyOnKeyBoard('up')
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        # print(asarray(image))
        if isCollide(data) == True:
            hitKeyOnKeyBoard('up')
            
        
