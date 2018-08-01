'''
image recognition pixel range:
    height: 768
    width:  1366
    The pixel value vary with respect to different screens
'''



from PIL import ImageGrab,ImageOps
import pyautogui as pg
import time
from numpy import *

class Cordinates():
    replayBtn = (481,504)
    dinosaur = (186,509) #654  #diff = 145
    #x = 240 for a tree to appear at
    #y= 545 for lowest obstacle size
def restartGame():
    pg.click(Cordinates.replayBtn)

def pressSpace():
    pg.keyDown('space')
    time.sleep(0.05)
    print("jump")
    pg.keyUp('space')

def imageGrab():
    box1 = (Cordinates.dinosaur[0]+60 ,Cordinates.dinosaur[1],Cordinates.dinosaur[0]+80,Cordinates.dinosaur[1]+36)
    image1 = ImageGrab.grab(box1)
    grayImage =  ImageOps.grayscale(image1)
    a = array(grayImage.getcolors())
    x=a.sum()
    print(x)
    return(x)



def main():
    restartGame()
    while True:
        if imageGrab()!=967:
            pressSpace()
            time.sleep(0.001)

main()


