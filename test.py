import threading
from time import sleep
import keyboard


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


def myFunction(arg):
    while event.is_set():
        print(arg)


if __name__ == "__main__":
    # initially unset, so workers will be paused at first
    event = threading.Event()
    processs = threading.Thread(target=listen_F3).run()
    event.wait()
    while event.wait():
        if(c == 4):
            continue
        for i in ['up', 'down', 'left', 'right']:
            threading.Thread(target=myFunction, name=i, args=(i,)).start()
            c += 1

        # wait for the rest of the work to be completed
