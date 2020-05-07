__author__ = "Tshark Online"
__license__ = "GPL"
__version__ = "2.5.0"

import pyautogui
from time import localtime, strftime, sleep, gmtime
from ctypes import Structure, windll, c_uint, sizeof, byref
from os import system
from random import randrange

pyautogui.FAILSAFE = False

class LASTINPUTINFO(Structure):
    _fields_ = [
        ('cbSize', c_uint),
        ('dwTime', c_uint),
    ]

def get_idle_duration():
    lastInputInfo = LASTINPUTINFO()
    lastInputInfo.cbSize = sizeof(lastInputInfo)
    windll.user32.GetLastInputInfo(byref(lastInputInfo))
    millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
    return millis / 1000.0

def cur_time():
    return strftime("%Y-%m-%d %H:%M:%S", localtime())

def convert(seconds): 
    return strftime("%H:%M:%S", gmtime(seconds)) 

print(f"{cur_time()}:Starting...")
inactive = 0  #keeps the inactive time everytime shift is pressed
local_idle = 0  #used to calculate the exact time being inactive
while(True):
    sys_idle_time = get_idle_duration()      
    if(sys_idle_time<1 and inactive!=0): 
        print(f"You were inactive for {convert(inactive+local_idle)}. Stay active!")
        inactive = 0    
    if(sys_idle_time>840):
        inactive+=sys_idle_time
        if(inactive>3600):
            print(f"You been inactive for {convert(inactive)}. Good Bye!")
            break
        else:
            pyautogui.press("shift")
            print(f"{cur_time()}:Shift pressed. Inactive for {convert(inactive)}")
            sleep(2)    
    else:
        local_idle = sys_idle_time
        if(sys_idle_time>59):  print(f"{cur_time()}: idle time:{convert(sys_idle_time)}") 
        sleep(randrange(30, 120))
system('pause')