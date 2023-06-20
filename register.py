import getStudentID
import collationMember
import readNFC
import addNFC
import addMember
import addNFC

# 学生IDとメールアドレスを取得
id, mail, idm = getStudentID.main()

if(collationMember.main()):
    # IDが登録済み
    addNFC.main(readNFC.main())
else:
    # IDが未登録
    addMember.main(id, mail)
    addNFC.main(id, idm)