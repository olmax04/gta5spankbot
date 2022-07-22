
import keyboard
from time import sleep
from script import startThread
import threading
from script import findByPixel


def invert_event(key_event):
    global c
    if event.is_set():
        event.clear()
        sleep(2)
        print("[Info] - Процесс приостановлен")
    else:
        print("[Info] - Процесс возобновлён")
        c = 0
        event.set()


def listen_F3():
    keyboard.on_release_key(key='F9', callback=invert_event)


def greeting():
    print(f"GTA5SPANKBOT v1.0 .by Olmax04")
    print(f"Push F9 to start and stop script")


def startThread(button):
    res = findByPixel(button)


def starting(button):
    while event.is_set():
        startThread(button)


if __name__ == "__main__":
    try:
        event = threading.Event()
        processs = threading.Thread(target=listen_F3).run()
        greeting()
        event.wait()
        while event.wait():
            if(c == 4):
                continue
            for i in ['up', 'down', 'left', 'right']:
                threading.Thread(target=starting, name=i, args=(i,)).start()
                c += 1  # creating event method  # hotkey method
    except Exception as e:
        print(e)
