import sys
from scapy.all import *


targetIP = raw_input("Target IP Address: ")

send (IP(dst=targetIP)/ICMP(), count = 9001)
