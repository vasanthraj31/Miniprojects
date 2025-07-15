# A GUI interface for the Screenshot Program
import time
import pyautogui
import tkinter as tk
def scree():
    name=int(round(time.time()*1000))
    name='D:/miniprojects1/scrrenshotdata/{}.png'.format(name)
    time.sleep(2)
    img=pyautogui.screenshot(name)
    img.show()
root=tk.Tk()
frame=tk.Frame(root)
frame.pack()

button=tk.Button(frame,text="Take Screenshot",command=scree)
button.pack(side=tk.LEFT)
close=tk.Button(frame,text="QUIT",command=quit)
close.pack(side=tk.RIGHT)
root.mainloop()
