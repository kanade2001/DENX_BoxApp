def collationMember(idm, updateStatus=True):
    # member.csvにidmが登録されていればusername，showname，statusを返す
    # updateStatus=Trueならstatusを更新(反転)
    # 登録されていなければnoneを返す
    print("collationMember", idm)
    
def collationNFC(idm):
    # nfc.csvにidmが登録されていればkeyidmを返す
    # 登録されていなければnoneを返す
    print("collationNFC", idm)
    
def addNFC(idm, keyidm):
    # nfc.csvにidm, userkeyのペアを登録
    print("addNFC", idm, keyidm)
