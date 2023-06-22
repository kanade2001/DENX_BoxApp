import readNFC
import display

def main():
    display.update("DEBUG MODE", "Touch NFC Tag")
    idm = readNFC.main()
    display.update("Your idm is", str(idm),waittime=10)