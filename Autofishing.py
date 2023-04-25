# -*- coding: utf-8 -*-
import time
from win32gui import GetWindowText, GetForegroundWindow
from tkinter import *
import threading

import fishing_op, util

class Threader(threading.Thread):

    def __init__(self, *args, **kwargs):
        threading.Thread.__init__(self, *args, **kwargs)
        self.daemon = True
        self.signal = False

    def run(self):
        while True:
            if self.signal:
                start_fishing()
            else:
                continue
    
    def stop_fishing(self):
        print("stop fishing")
        self.signal = False
    
    def start_fishing(self):
        print("start fishing")
        self.signal = True

def start_fishing():
    util.set_work_dir()
    now = time.time()
    try:
        if GetWindowText(GetForegroundWindow()) == "World of Warcraft" or GetWindowText(GetForegroundWindow()) == "魔兽世界":
            fishing_op.working(now)
    except:
        print("stop fishing")

def create_a_new_thread():
    thread = Threader(name='Play-Thread')
    thread.start()
    return thread

if __name__ == "__main__":
    root = Tk()
    root.title('张靖宜的钓鱼外挂')
    root.geometry("300x100")
    leftFrame = Frame(root)
    leftFrame.pack(side=LEFT)
    rightFrame = Frame(root)
    rightFrame.pack(side=RIGHT)
    thread = create_a_new_thread()
    playButton = Button(leftFrame, text="开始钓鱼", fg="blue")
    playButton['command'] = thread.start_fishing
    stopButton = Button(rightFrame, text="停止钓鱼", fg="red")
    stopButton['command'] = thread.stop_fishing
    playButton.pack(side=TOP)
    stopButton.pack(side=BOTTOM)
    root.mainloop()