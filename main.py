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
        elif idm == settings.IDM_DEBUG:
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

def clock():
    while True:
        now = datetime.datetime.now().date() + " " + datetime.datetime.now().time().isoformat(timespec='seconds')
        now = str(datetime.datetime.now().date()) + " " + str(datetime.datetime.now().time().isoformat(timespec='seconds'))
        display.update("DENX BOX 233", now, 0)

def runserver():
    server.RUN()

async def main():
    print("start")
    threading.Thread(target=read).start()
    threading.Thread(target=disp).start()
    threading.Thread(target=clock).start()
    threading.Thread(target=runserver).start()

if __name__ == "__main__":
    main()
