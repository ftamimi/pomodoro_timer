#!/usr/bin/env python3
# Python 3.x code
# Imports
import tkinter
from pygame import mixer
from tkinter import messagebox
import datetime
import time

def run_alert(message):
    # This code is to hide the main tkinter window
    print('Starting 25 min timer...')
    now = datetime.datetime.now()
    print ("Current date and time : ")
    print (now.strftime("%Y-%m-%d %H:%M:%S"))
    current_time= now.strftime("%Y-%m-%d %H:%M:%S")
    print()
    root = tkinter.Tk()
    root.wm_attributes("-topmost", 1)
    root.withdraw()
    # a = tkinter.Label(root, text=f"Current date and time : {current_time}")
    # a.pack()
    # root.mainloop()

    time.sleep(1500)


    # Message Box
    print('Timer done')
    now = datetime.datetime.now()
    print ("Current date and time : ")
    print (now.strftime("%Y-%m-%d %H:%M:%S"))
    mixer.init()
    mixer.music.load('alarm.mp3')
    mixer.music.play()

    messagebox.showinfo("PomoTimer", message, parent=root)


if __name__=="__main__":
    run_alert("Time's up")