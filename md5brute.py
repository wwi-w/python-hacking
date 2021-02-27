from termcolor import colored
import hashlib

def tryOpen(wordlist):
    global pass_file
    try:
        pass_file = open(wordlist, "r")
    except:
        print(" no such file ")
        quit()

pass_hash=input("md5 password ")
wordlist =input("password list file")
tryOpen(wordlist)

for word in pass_file:
    print(colored(" trying " + word.strip("\n"), 'red'))
    enc_wrd = word.encode('utf-8')
    md5gest= hashlib.md5(enc_wrd.strip()).hexdigest()

    if md5gest==pass_file:
        print("password found " + word )