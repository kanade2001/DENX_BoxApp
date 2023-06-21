import readNFC
import socket

import accessDatabase

# 学生IDとメールアドレスを取得
def main():
    id, mail, idm = readNFC.getStudentID()
    if accessDatabase.collationNFC(idm):
        # idmが登録済み
        accessDatabase.addNFC(readNFC.main(), idm)
    else:
        # IDが未登録
        sendMail(id, mail, idm)

def sendMail(studentID, mail, nfcID):
    IP = socket.gethostbyname(socket.gethostname())
    url = "http://" + str(IP) + ":8000?sid=" + str(studentID) + "&nid=" + str(nfcID)