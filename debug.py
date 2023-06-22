import readNFC
import display
import time

def main():
    display.update("DEBUG MODE", "Touch NFC Tag")
    idm = readNFC.main()
    display.update("Your idm is", str(idm),waittime=10)
    time.sleep(10)
    display.update(None, None)