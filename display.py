import drivers
import time

str1 = ""
str2 = ""
showlimit = time.time()

def main():
    global str1
    global str2
    display = drivers.Lcd()
    display.lcd_display_string(str1, 1)
    display.lcd_display_string(str2, 2)

def update(line1, line2, waittime=60):
    global str1
    global str2
    global showlimit
    if waittime != 0:
        str1 = line1
        str2 = line2
        showlimit = time.time() + waittime
    elif time.time() > showlimit:
        str1 = line1
        str2 = line2