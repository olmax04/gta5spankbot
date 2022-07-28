from http.client import responses
import sys
import keyboard
from time import sleep
from script import startThread
import script
import threading
import pyautogui
import requests

exit = False
c = 0


def run_once(f):
    global wrapper

    def wrapper(*args):
        if not wrapper.has_run:
            wrapper.has_run = True
            return f(*args)
    wrapper.has_run = False
    return wrapper


@run_once
def check(key):
    lock.acquire()
    r = requests.post(
        "https://bot.olmaxdeveloper.online/api/check", json={'key': key})
    response = r.json()
    # print(response)
    match response["status"]:
        case "active": lock.release()
        case "expired":
            print(response["message"])
            stop()
        case "blocked":
            print(response["message"])
            stop()


def stop(key_event):
    global exit
    if(event.is_set()):
        event.clear()
        script.d = 0
        sleep(2)
        run_once(print("[INFO] - Process stopped"))
    else:
        print("Exiting...")
        sleep(3)
        exit = True
        event.set()


def start(key_event):
    global c
    check(key_var)
    if not (event.is_set()):
        c = 0
        script.d = 0
        script.restart = True
        script.pause = False
        print(f"[INFO] - Process started")
        event.set()


def listen_F3():
    keyboard.on_release_key(key='F9', callback=stop)
    keyboard.on_release_key(key='E', callback=start)


def starting(button):
    while event.is_set():
        if(script.restart == True):
            if(script.pause == True):
                check(key_var)
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


def script_start(key):
    global event, c, exit, lock, key_var
    key_var = key
    try:
        lock = threading.Lock()
        event = threading.Event()
        process = threading.Thread(target=listen_F3)
        process.start()
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
        input()
# if __name__ == "__main__":
#     try:
#         event = threading.Event()
#         process = threading.Thread(target=listen_F3)
#         process.start()
#         event.wait()
#         while event.wait():
#             if(exit == True):
#                 break
#             if(c == 4):
#                 continue
#             for i in ['up', 'down', 'left', 'right']:
#                 threading.Thread(target=starting, name=i, args=(i,)).start()
#                 c += 1
#         sys.exit()
#     except Exception as e:
#         print(e)
