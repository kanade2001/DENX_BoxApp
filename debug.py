import readNFC
import display
import time

def main():
    display.update("DEBUG MODE", "Touch NFC Tag")
    idm = readNFC.main()
    display.update("Your idm is", str(idm))
    time.sleep(10)
    display.update(None, None)