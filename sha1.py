import urllib.request
from termcolor import colored
import urlopen

import hashlib
shalhash = input("[+] enter sha1 hash value: ")
passlist = open(str('pass.txt'), 'utf-8')

for password in passlist:
    hashgues = hashlib.sha1(bytes(password), 'utf-8').hexdigest()
    if hashgues ==shalhash:
        print(colored("[+] the password is : " + str(password),'green'))
        quit()
    else:
        print(colored("[-] password guess " + str(password) + " does not match, trying next....",'red'))
print("password not in password list")
