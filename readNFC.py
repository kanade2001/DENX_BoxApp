import nfc
import binascii
import time
import wrapt_timeout_decorator
import settings

lastreadtime = time.time()

@wrapt_timeout_decorator.timeout(dec_timeout=settings.DISPLAY_TIME_WAIT)
def main():
    global lastreadtime
    while lastreadtime > time.time():
        pass
    clf = nfc.ContactlessFrontend('usb')
    tag = clf.connect(rdwr={'targets': ['212F', '424F'], 'on-connect': lambda tag: False}) # Type3Tagを取得
    idm = binascii.hexlify(tag.idm).decode() # 固有IDの抽出
    lastreadtime = time.time() + settings.DISPLAY_TIME_COMPLETE
    return idm

@wrapt_timeout_decorator.timeout(dec_timeout=settings.DISPLAY_TIME_WAIT)
def getStudentID():
    global lastreadtime
    while lastreadtime > time.time():
        pass
    clf = nfc.ContactlessFrontend('usb')
    tag = clf.connect(rdwr={'targets': ['212F', '424F'], 'on-connect': lambda tag: False})

    service_code_id = 0x1a8B
    service_code_mail = 0x200B

    #システムコード指定（指定しなければ最初に見つかった12FCが読まれる）
    idm, pmm = tag.polling(system_code=0xfe00)
    tag.idm, tag.pmm, tag.sys = idm, pmm, 0xfe00
    sc = nfc.tag.tt3.ServiceCode(service_code_id >> 6, service_code_id & 0x3f)
    bc = nfc.tag.tt3.BlockCode(0,service=0)
    data = tag.read_without_encryption([sc],[bc])
    StuID = data[1:12].decode()
    

    idm, pmm = tag.polling(system_code=0x8bb3)
    tag.idm, tag.pmm, tag.sys = idm, pmm, 0x8bb3
    sc = nfc.tag.tt3.ServiceCode(service_code_mail >> 6, service_code_mail & 0x3f)
    bc = nfc.tag.tt3.BlockCode(0,service=0)
    data = tag.read_without_encryption([sc],[bc])
    Mail = data[0:9].decode()
    Mail += "@doshisha.ac.jp"
    
    idm = binascii.hexlify(tag.idm).decode()
    
    lastreadtime = time.time() + settings.DISPLAY_TIME_COMPLETE

    return StuID, Mail, idm

if __name__ == "__main__":
    print(main())