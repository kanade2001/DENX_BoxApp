import readNFC
import display

def main():
    try:
        idm = readNFC.main()
    except TimeoutError:
        return

    display.update("Your idm is", idm)