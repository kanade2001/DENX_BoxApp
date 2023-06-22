import drivers
import time
import datetime

str1 = None
str2 = None
showlimit = time.time()
display = drivers.Lcd()

def main():
    if str1 == None:
        str1 = "DENX BOX 233"
    if str2 ==None:
        str2 = str(datetime.datetime.now().date())[5:] + " " + str(datetime.datetime.now().time().isoformat(timespec='seconds'))
    display.lcd_display_string(str1, 1)
    display.lcd_display_string(str2, 2)

def update(line1, line2):
    global str1
    global str2
    str1 = line1
    str2 = line2