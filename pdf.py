import pikepdf
from tqdm import tqdm
## COLORS ###############
wi="\033[1;37m" #>>White#
rd="\033[1;31m" #>Red   #
gr="\033[1;32m" #>Green #
yl="\033[1;33m" #>Yellow#
#########################

# load password list
wordlist =input ("path to your worlist: ")
pdff = input ("path to your pdf: ") 
passwords = [ line.strip() for line in open(wordlist) ]

# iterate over passwords
print("congratulation wait for a minute i will crack the password with the wordlist you provided wait....")
for password in tqdm(passwords, "Decrypting PDF"):
    try:
        # open PDF file
        with pikepdf.open(pdff, password=password) as pdf:
            # Password decrypted successfully, break out of the loop
            print(yl+"[+] Password found: "+gr + password)
            break
    except pikepdf._qpdf.PasswordError as e:
        # wrong password, just continue in the loop
        continue
