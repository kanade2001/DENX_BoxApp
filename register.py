import socket
import readNFC
import display
import accessDatabase

# 学生IDとメールアドレスを取得
def main():
    try:
        id, mail, idm = readNFC.getStudentID()
        if accessDatabase.collationNFC(idm):
            # idmが登録済み
            username, showname, status = accessDatabase.collationMember(idm, False)
            accessDatabase.addNFC(readNFC.main(), idm)
        else:
            # IDが未登録
            sendMail(id, mail, idm)
            display.update("Send mail to",str(mail)[:13] + "...")
    except Exception as err:
        pass

def sendMail(studentID, mail, nfcID):
    IP = socket.gethostbyname(socket.gethostname())
    url = "http://" + str(IP) + ":8000?sid=" + str(studentID) + "&nid=" + str(nfcID)