import time
import pyautogui
def scree():
    name=int(round(time.time()*1000))
    name='D:/miniprojects1/scrrenshotdata/{}.png'.format(name)
    time.sleep(2)
    img=pyautogui.screenshot(name)
    img.show()
scree()