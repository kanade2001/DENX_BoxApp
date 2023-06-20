import readNFC
import collationNFC
import sendMessageToDiscord
import register
import debug
import settings

idm = readNFC.main()

if idm == settings.IDM_REGISTER:
    register.main()
elif idm == settings.IDM_DEBUG:
    debug.main()
else:
    username = collationNFC.main()
    if username != None:
        sendMessageToDiscord.main(username)