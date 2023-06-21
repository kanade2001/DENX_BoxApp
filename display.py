import drivers
from time import sleep


def main(line1, line2, waittime=60):
    display = drivers.Lcd()
    display.lcd_display_string(line1, 1)
    display.lcd_display_string(line2, 2)
    sleep(waittime)
    
if __name__ == "__main__":
    main("Denxchang","sample abc 123")