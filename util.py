import cv2
import numpy as np
import screen_cap
import time
import os, sys
import pyautogui, random

work_dir = ""


def set_work_dir():
    global work_dir
    work_dir = os.getcwd()+"\images"


def get_work_dir():
    global work_dir
    return work_dir


def find_match(img_rgb, prefix, max, threshold=0.50):
    print("Looking for float {}".format(time.time()))
    # todo: maybe make some universal float without background?

    #images_path = os.path.join(get_work_dir(), "images")
    
    for x in range(0, max):
        target_path = os.path.join(work_dir, prefix + "_" + str(x) + ".png")
        template = cv2.imread(target_path, 0)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

        try:
            w, h = template.shape[::-1]
            res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
            loc = np.where(res >= threshold)

            for pt in zip(*loc[::-1]):
                cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

            if loc[0].any():
                return [(loc[1][0] + w / 2), (loc[0][0] + h / 2), img_rgb]
        except Exception as e:
            print(e)

    return None


def find_float():
    return find_match(screen_cap.screen_img_np(), "float", 6)


def move_mouse_to_center_up():
    area = screen_cap.window_area()
    pyautogui.moveTo(
        int(area[2] / 2),
        int(area[3] / 2) - random.randint(50, 120),
        random.uniform(0.1, 0.5),
    )


def move_mouse_to_center():
    area = screen_cap.window_area()
    pyautogui.moveTo(
        int(area[2] / 2),
        int(area[3] / 2) + random.randint(10, 20),
        random.uniform(0.1, 0.5),
    )


def move_mouse_rand():
    area = screen_cap.window_area()
    pyautogui.moveTo(
        random.randint(area[0], area[2]),
        random.randint(area[1], area[3]),
        random.uniform(0.15, 0.25),
    )

