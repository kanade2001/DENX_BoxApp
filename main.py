import asyncio
import readNFC
import accessDatabase
import sendMessageToDiscord
import register
import debug
import server
import display
import settings
import datetime
import threading

def read():
    while True:
        try:
            idm = readNFC.main()
        except TimeoutError:
            continue

        if idm == settings.IDM_REGISTER:
            register.main()
        #elif idm == settings.IDM_DEBUG:
        elif True:
            debug.main()
        else:
            username, showname, status = accessDatabase.collationMember(idm)
            if username != None:
                if status == True:
                    display.update("See you", showname, settings.DISPLAY_TIME_COMPLETE)
                else:
                    display.update("Hello", showname, settings.DISPLAY_TIME_COMPLETE)
                sendMessageToDiscord.main(username, status)

def disp():
    while True:
        display.main()

def runserver():
    server.RUN()

def main():
    print("start")
    thread_1 = threading.Thread(target=read)
    thread_2 = threading.Thread(target=disp)
    thread_3 = threading.Thread(target=runserver)
    
    thread_1.start()
    thread_2.start()
    thread_3.start()

if __name__ == "__main__":
    main()
