import readNFC
import display

def main():
    try:
        idm = readNFC.main()
        display("IDM:", idm)
    except Exception as err:
        pass