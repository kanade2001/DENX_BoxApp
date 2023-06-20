import nfc
import binascii

def main():
    clf = nfc.ContactlessFrontend('usb')
    tag = clf.connect(rdwr={'targets': ['212F', '424F'], 'on-connect': lambda tag: False}) # Type3Tagを取得
    idm = binascii.hexlify(tag.idm).decode() # 固有IDの抽出
    return idm

if __name__ == "__main__":
    print(main())


