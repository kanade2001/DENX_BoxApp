import readNFC
import display

def main():
    display.update("DEBUG MODE", "Touch NFC Tag")
    try:
        idm = readNFC.main()
    except TimeoutError:
        return

    display.update("Your idm is", idm)