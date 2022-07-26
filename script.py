from time import sleep
import pyautogui
import random

restart = True
pause = False
d = 0


def findByPixel(button):
    global restart, d
    match button:
        case "down":
            x = [958, 962, 960]
            y = [840, 840, 841]
        case "up":
            x = [956, 964, 961]
            y = [824, 824, 823]
        case "left":
            x = [953, 953, 952]
            y = [830, 836, 832]
        case "right":
            x = [968, 968, 969]
            y = [830, 835, 833]
    i = 0
    for a, b in zip(x, y):
        pix = pyautogui.pixelMatchesColor(a, b, (255, 255, 255), tolerance=254)
        match pix:
            case False:
                i += 1
                if(i == 3):
                    d = 0
                    restart = True
                    click(button)
                    print(f"[Успех] - Клавиша нажата '{button}'")
            case True:
                break


def click(button):
    pyautogui.press(button)


def startThread(button):
    global d, pause
    res = findByPixel(button)
    if(res == None):
        if(d == 75 or d == 150):
            pause = True
        elif(pause == True):
            return
        d += 1


# --------------------------Методы-------------------------------
# def screen():
#     pyautogui.screenshot("test.png", region=(914, 785, 90, 90))


# def findByImage(value):
#     try:
#         button = pyautogui.locateOnScreen(
#             f"{value}.png", region=(914, 785, 90, 90))
#         print(button)
#         if button != None:
#             pyautogui.press(value)
#             print(f"[Успех] - Нажата кнопка {value}")
#             return
#         # print(f"[Ошибка] - Не клавиша {value}")
#         # print(f"[Данные] - {button}")
#         return
#     except Exception as e:
#         print(f"{e}")
# def start():
#     for button in ["up", "left", "right", "down"]:
#         res = findByPixel(button)
#         match res:
#             case True:
#                 click(button)
#                 print(f"[Успех] - Клавиша нажата '{button}'")
#             case False:
#                 pass

# --------------------------Координаты-------------------------------
# case "down":
#     x = [960, 957, 964]
#     y = [841, 839, 839]
# case "up":
#     x = [957, 961, 964]
#     y = [825, 823, 825]
# case "left":
#     x = [953, 952, 953]
#     y = [830, 833, 836]
# case "right":
#     x = [968,969, 968]
#     y = [830,833, 836]

# case "down":
#     x = [958, 962, 960]
#     y = [840, 840, 841]
# case "up":
#     x = [956, 964, 961]
#     y = [824, 824, 823]
# case "left":
#     x = [953, 953, 952]
#     y = [830, 836, 832]
# case "right":
#     x = [968, 968, 969]
#     y = [830, 835, 833]
