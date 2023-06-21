def collationMember(idm):
    # member.csvにidmが登録されていればusernameとstatusを返し，statusを更新
    # 登録されていなければnoneを返す
    print("collationMember", idm)
    
def collationNFC(idm):
    # nfc.csvにidmが登録されていればkeyidmを返す
    # 登録されていなければnoneを返す
    print("collationNFC", idm)
    
def addNFC(idm, keyidm):
    # nfc.csvにidm, userkeyのペアを登録
    print("addNFC", idm, keyidm)
