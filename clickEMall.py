import ctypes
import os
import time
from pynput import keyboard
from pynput.keyboard import Controller as kbd_controller
from pynput.keyboard import Key
from random import uniform

working_dir = os.path.dirname(os.path.realpath(__file__))
print()
print("Script directory: " + working_dir)
print("cports.exe must be in above dir")
title = "Background POE Task"
os.system('title ' + title)
os.system('color 30')

def minimize():
    user32 = ctypes.windll.user32
    h_wnd = user32.GetForegroundWindow()
    user32.ShowWindow(h_wnd, 6)
minimize()

cports = working_dir+r"\cports.exe /close * * * * PathOfExile_x64Steam.exe"
kill_poe = 'taskkill /F /FI "WINDOWTITLE eq Path of Exi*" /IM * /T'

kbd = kbd_controller()
s1 = "`"
s2 = "<Shift>+<Ctrl>" #need to release keys in logout v
s3 = "c+x"
sExit = "<Shift>+<Esc>"

t1 = "12345"
t2 = "Log out from poe"
t3 = "Cut connection to poe"

l_m = {s1: t1, s2:t2, s3: t3}
message = "Click {} to {}."
print()
print("===============Click All===================")
print()
for k, v in l_m.items():
    print(message.format(k, v))
print()
print("To exit script press {}".format(sExit))

def press_buttons(c):
    kbd.press(c)
    kbd.release(c)
    a = uniform(0.01, 0.09)
    time.sleep(a)

def clikAll():
    kbd.release(s1)
    for c in t1:
        press_buttons(c)

def logOut():
    kbd.release(Key.ctrl)
    kbd.release(Key.shift)
    os.system(kill_poe)

def tcp_dc():
    kbd.release(s3[-1:])
    kbd.release(s3[:1])
    os.system(cports)

def stop_script():
    h.stop()
    


with keyboard.GlobalHotKeys({
        s1: clikAll,
        s2: logOut,
        s3: tcp_dc,
        sExit: stop_script}) as h:
    h.join()