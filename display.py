import drivers
import time
import datetime

str1 = None
str2 = None
showlimit = time.time()
display = drivers.Lcd()

def main():
    display.lcd_display_string(str1 if str1 != None else "DENX BOX 233   ", 1)
    display.lcd_display_string(str2 if str2 != None else str(datetime.datetime.now().date())[5:] + " " + str(datetime.datetime.now().time().isoformat(timespec='seconds')) + "  ", 2)

def update(line1, line2):
    global str1
    global str2
    if line1 == None:
        str1 = None
    else:
        str1 = line1.ljust(16)
    if line2 == None:
        str2 = None
    else:
        str2 = line2.ljust(16)