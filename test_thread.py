import threading
from time import sleep


def threads(button):
    while True:
        lock.acquire()
        if(button == 'up'):
            sleep(3)
            print("test")
            lock.release()
        print("work" + button)


if(__name__ == "__main__"):
    lock = threading.Lock()
    for i in ["up", "down"]:
        threading.Thread(target=threads, args=(i,)).start()
