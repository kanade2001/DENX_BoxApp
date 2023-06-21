import readNFC
import accessDatabase
import sendMessageToDiscord
import register
import debug
import server
import settings

def main():
    idm = readNFC.main()

    if idm == settings.IDM_REGISTER:
        register.main()
    elif idm == settings.IDM_DEBUG:
        debug.main()
    else:
        username, status = accessDatabase.collationMember(idm)
        if username != None:
            sendMessageToDiscord.main(username, status)

if __name__ == "__main__":
    server.RUN()
    while True:
        main()