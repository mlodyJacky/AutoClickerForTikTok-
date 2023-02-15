from pyautogui import *
import pyautogui
import time
import keyboard
import win32api
import win32
import cv2


i=0
stan="obserwowanie"
odklikniecia=0
klikniecia=0
sleep(3)
while keyboard.is_pressed('q') == False:
    i+=1
    while stan=="obserwowanie":
        if keyboard.is_pressed('q') == True:
            break
        x, y=pyautogui.center(pyautogui.locateOnScreen("obserwuj.PNG", confidence=0.75,region=(1380,20, 503, 915)))
        pyautogui.moveTo(x, y, duration = 0.1)
        pyautogui.click(x,y)
        print("KLIKNALEM", klikniecia)
        klikniecia+=1
        if klikniecia==19:
            klikniecia==0
            stan="powrot1"
        if klikniecia==11:
            pyautogui.moveTo(1656, 902, duration = 0.1)
            pyautogui.scroll(-400)
        sleep(0.5)
    if stan=="powrot1":
        pyautogui.moveTo(1656, 902, duration = 0.1)
        pyautogui.scroll(400)
        sleep(0.5)
        pyautogui.moveTo(1656, 902, duration = 0.1)
        pyautogui.scroll(400)
        stan="odobserwowanie"
        sleep(1)

    if stan=="powrot2":
        pyautogui.moveTo(1656, 902, duration = 0.1)
        pyautogui.scroll(400)
        sleep(0.5)
        pyautogui.moveTo(1656, 902, duration = 0.1)
        pyautogui.scroll(400)
        stan="obserwowanie"
        sleep(1)

    while stan=="odobserwowanie":
        if keyboard.is_pressed('q') == True:
            break
        x, y=pyautogui.center(pyautogui.locateOnScreen("obserwowani.PNG", confidence=0.60,region=(1380,20, 503, 915)))
        pyautogui.moveTo(x, y, duration = 0.1)
        pyautogui.click(x,y)
        print("ODKLIKNALEM ", odklikniecia)
        odklikniecia+=1
        if odklikniecia==19:
            odklikniecia=0
            stan="powrot2"
        if odklikniecia==10:
            pyautogui.moveTo(1656, 902, duration = 0.1)
            pyautogui.scroll(400)
        sleep(0.5)




