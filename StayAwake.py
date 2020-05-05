__author__ = "Tshark Online"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Tshark"
__status__ = "Production"

from pyautogui import press
from time import localtime, strftime, sleep
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

print(f"{cur_time()}:Starting...")
inactive = 0
while(True):
    idle_time = get_idle_duration()      
    if(idle_time<1): inactive = 0    
    if(idle_time>300):
        if(inactive>3600):
            print(f"You been inactive for {(inactive/60)/60}hr. Good Bye!")
            break
        else:
            inactive+=idle_time
            press("shift")
            print(f"{cur_time()}:Shift pressed. Inactive for {(inactive/60)}m")
            sleep(2)    
    else:
        print(f"{cur_time()}: idle time:{idle_time}") 
        sleep(30)