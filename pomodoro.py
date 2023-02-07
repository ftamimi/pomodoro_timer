# Python 3.x code
# Imports
import tkinter
from tkinter import messagebox
import datetime
import time

def run_alert(message):
    # This code is to hide the main tkinter window
    print('Starting 25 min timer...')
    now = datetime.datetime.now()
    print ("Current date and time : ")
    print (now.strftime("%Y-%m-%d %H:%M:%S"))
    print()
    time.sleep(1500)
    root = tkinter.Tk()
    root.wm_attributes("-topmost", 1)
    root.withdraw()

    # Message Box
    print('Timer done')
    now = datetime.datetime.now()
    print ("Current date and time : ")
    print (now.strftime("%Y-%m-%d %H:%M:%S"))

    messagebox.showinfo("PomoTimer", message, parent=root)


if __name__=="__main__":
    run_alert("Time's up")