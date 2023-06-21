import readNFC
import accessDatabase
import sendMessageToDiscord
import register
import debug
import server
import display
import settings

def main():
    idm = readNFC.main()

    if idm == settings.IDM_REGISTER:
        register.main()
    elif idm == settings.IDM_DEBUG:
        debug.main()
    else:
        username, showname, status = accessDatabase.collationMember(idm)
        if username != None:
            sendMessageToDiscord.main(username, status)
            if status == True:
                display.main("See you", showname)
            else:
                display.main("Hello", showname)

if __name__ == "__main__":
    server.RUN()
    while True:
        main()