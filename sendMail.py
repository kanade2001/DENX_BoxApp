import socket

def main(studentID, mail, nfcID):
    IP = socket.gethostbyname(socket.gethostname())
    url = "http://" + str(IP) + ":8000?sid=" + str(studentID) + "&nid=" + str(nfcID)

    

if __name__ == "__main__":
    print(main(1116, "cguf", "xxxx"))
    