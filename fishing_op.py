import pyautogui, random, time
import util
import numpy as np
import cv2
from matplotlib import pyplot as plt

pyautogui.FAILSAFE = False

RECAST_TIME = 30 + 2
DO_BAIT_TIME = 10 * 60 + 10

is_block = False
begin_time = time.time()
new_cast_time = 0
frame_count = 0
lastx = 0
lasty = 0

stat = {"do_bait": 0, "casting": 0, "catch": 0, "throw_rubbish": 0, "open_shell": 0}


def move_mouse_to(x, y):
    pyautogui.moveTo(x, y, random.uniform(0.15, 0.35))

    pyautogui.FAILSAFE


def snatch(x, y):
    pyautogui.moveTo(x, y, random.uniform(0.08, 0.15))

    pyautogui.mouseDown(button="right")
    pyautogui.mouseUp(button="right")


def move_mouse_to_free_area():
    time.sleep(random.uniform(2.0, 3.3))
    move_mouse_to(
        30, 30,
    )


def get_area(hight, width):
    return hight * width


def get_fish(avg_place, place, img_rgb):
    print("detected!")
    print("avg_place: ", avg_place)
    print("place:", place)
    threshold = 2 + (avg_place[1] - 550) / 150
    print("threshold: ", threshold)
    if place[1] - avg_place[1] >= threshold:
        # plt.imshow(img_rgb)
        # plt.title("template"), plt.xticks([]), plt.yticks([])
        # plt.show()
        return True
    return False


def jump():
    pyautogui.press("space")


def end_fishing():
    print("收杆")
    time.sleep(random.uniform(0.2, 0.4))
    move_mouse_to_free_area()


def do_bait(now):
    print("抛竿")
    pyautogui.press("b")
    time.sleep(random.uniform(1.5, 2))
    avg_place = 0
    while True:
        if time.time() - now >= 20:
            end_fishing()
            break
        place = util.find_float()
        if place:
            if avg_place == 0:
                avg_place = place[:2]
            else:
                if (
                    place[0] - avg_place[0] > 10
                    or avg_place[0] - place[0] > 10
                    or avg_place[1] - place[1] > 10
                    or place[1] - avg_place[1] > 10
                ):
                    continue
                if get_fish(avg_place, place[:2], place[2]):
                    pyautogui.moveTo(place[0], place[1], random.uniform(0.1, 0.3))
                    pyautogui.click(button="right")
                    end_fishing()
                    break
                else:
                    avg_place = (
                        (avg_place[0] + place[0]) / 2,
                        (avg_place[1] + place[1]) / 2,
                    )


def working(now):

    do_bait(now)

    # Here sleep at least 3 second for bobber disapper
    time.sleep(random.uniform(1, 1.5))

