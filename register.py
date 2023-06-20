import getStudentID
import collationMember
import readNFC
import addNFC
import sendMail

# 学生IDとメールアドレスを取得
def main():
    id, mail, idm = getStudentID.main()

    if collationMember.main():
        # IDが登録済み
        addNFC.main(idm, readNFC.main())
    else:
        # IDが未登録
        sendMail.main(id, mail, idm)