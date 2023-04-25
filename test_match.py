import cv2
import numpy as np
import os
from matplotlib import pyplot as plt

truth_path = "D:\\Game_plugin\\wow-auto-fishing\\images\\test.png"
target_path = "D:\\Game_plugin\\wow-auto-fishing\\images\\float_5.png"
img = cv2.imread(truth_path, 0)
template = cv2.imread(target_path, 0)
methods = [
    "cv2.TM_CCOEFF",
    "cv2.TM_CCOEFF_NORMED",
]
w, h = template.shape[::-1]
for meth in methods:
    method = eval(meth)
    # Apply template Matching
    res = cv2.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(img, top_left, bottom_right, 255, 2)
    plt.subplot(121), plt.imshow(res, cmap="gray")
    plt.title("Matching Result"), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(img, cmap="gray")
    plt.title("Detected Point"), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)
    plt.show()
