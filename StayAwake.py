__author__ = "Tshark Online"
__license__ = "GPL"
__version__ = "2.0.0"

from pyautogui import press
from time import localtime, strftime, sleep, gmtime
from ctypes import Structure, windll, c_uint, sizeof, byref

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
inactive = 0
while(True):
    idle_time = get_idle_duration()      
    if(idle_time<1): inactive = 0    
    if(idle_time>300):
        if(inactive>3600):
            print(f"You been inactive for {convert(inactive)}. Good Bye!")
            break
        else:
            inactive+=idle_time
            press("shift")
            print(f"{cur_time()}:Shift pressed. Inactive for {convert(inactive)}")
            sleep(2)    
    else:
        print(f"{cur_time()}: idle time:{idle_time}") 
        sleep(60)