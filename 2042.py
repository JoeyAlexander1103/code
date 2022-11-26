
import os
import pyautogui
import cv2
import operator
import time
import msvcrt
def moveto(intx, inty):
    pyautogui.moveTo(intx, inty)

def findcolor(stax, stay, endx, endy, res):
    he, we = int(endx - stax),int(endy - stay)
    im = pyautogui.screenshot(region=(stax, stay, he, we))
    im.save("autoprt.png")
    im = cv2.imread("autoprt.png")
    for a in range(we):
        for b in range(he):
            if all(operator.eq(im[a,b], res)):
                moveto(stax + b, stay + a)
                os.remove("autoprt.png")
                return stax + b, stay + a



def delay(tim):
    time.sleep(tim/1000)

def keypress(kb):
    pyautogui.keyDown(kb)
    delay(300)
    pyautogui.keyUp(kb)


while True:

        pyautogui.doubleClick(findcolor(720, 146, 1010, 623, [0, 255, 0]))
        delay(100)
        pyautogui.doubleClick( findcolor(720, 146, 1010, 623, [223, 255, 38]))

