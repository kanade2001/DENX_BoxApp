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

async def read():
    while True:
        try:
            idm = readNFC.main()
        except Exception as err:
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

async def disp():
    while True:
        display.main()

async def clock():
    while True:
        now = datetime.datetime.now().date() + " " + datetime.datetime.now().time().isoformat(timespec='seconds')
        now = str(datetime.datetime.now().date()) + " " + str(datetime.datetime.now().time().isoformat(timespec='seconds'))
        display.update("DENX BOX 233", now, 0)

async def main():
    await asyncio.gather(read, disp, clock)

if __name__ == "__main__":
    server.RUN()
