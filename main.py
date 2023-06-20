import readNFC
import collationNFC
import sendMessageToDiscord
import register
import debug
import settings

def main():
    idm = readNFC.main()

    if idm == settings.IDM_REGISTER:
        register.main()
    elif idm == settings.IDM_DEBUG:
        debug.main()
    else:
        username, status = collationNFC.main()
        if username != None:
            sendMessageToDiscord.main(username, status)

if __name__ == "__main__":
    while True:
        main()