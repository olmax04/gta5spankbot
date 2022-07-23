import sys
import keyboard
from time import sleep
from script import startThread
import script
import threading
import pyautogui
import random

exit = False
c = 0


def stop(key_event):
    global exit
    if(event.is_set()):
        event.clear()
        script.d = 0
        sleep(2)
        print("[Info] - Процесс приостановлен")
    else:
        print("Выход из приложения...")
        sleep(3)
        exit = True
        event.set()


def start(key_event):
    global c
    if not (event.is_set()):
        print("[Info] - Процесс возобновлён")
        c = 0
        script.d = 0
        script.restart = True
        script.pause = False
        event.set()


def listen_F3():
    keyboard.on_release_key(key='F9', callback=stop)
    keyboard.on_release_key(key='E', callback=start)


def greeting():
    print(f"GTA5SPANKBOT v1.0 .by Olmax04")
    print(f"Push 'E' to start and 'F9' to exit script")


def starting(button):
    while event.is_set():
        if(script.restart == True):
            if(script.pause == True):
                # print(f"[Info] - Restarting... ['{button}']")
                script.restart = False
                script.pause = False
                pyautogui.press("E")
            else:
                startThread(button)
        elif(script.restart == False):
            if(script.pause == True):
                stop(button)
            else:
                startThread(button)


if __name__ == "__main__":
    try:
        event = threading.Event()
        process = threading.Thread(target=listen_F3)
        process.start()
        greeting()
        event.wait()
        while event.wait():
            if(exit == True):
                break
            if(c == 4):
                continue
            for i in ['up', 'down', 'left', 'right']:
                threading.Thread(target=starting, name=i, args=(i,)).start()
                c += 1
        sys.exit()
    except Exception as e:
        print(e)
