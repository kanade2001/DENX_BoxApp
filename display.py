import drivers
import time
import datetime

str1 = ""
str2 = ""
showlimit = time.time()
display = drivers.Lcd()

def main():
    display.lcd_display_string(str1, 1)
    display.lcd_display_string(str2, 2)

def update(line1, line2, waittime=60, align="left"):
    global str1
    global str2
    global showlimit
    if align == "left":
        line1 = line1.ljust(16)
        line2 = line2.ljust(16)
    elif align == "center":
        line1 = line1.center(16)
        line2 = line2.center(16)
    elif align == "right":
        line1 = line1.rjust(16)
        line2 = line2.rjust(16)
        
    if waittime != 0:
        str1 = line1
        str2 = line2
        showlimit = time.time() + waittime
    elif time.time() > showlimit:
        str1 = line1
        str2 = line2