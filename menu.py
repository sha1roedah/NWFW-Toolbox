# Program to test the functionality of network firewalls

# This menu is designed using a Juniper Netscreen 5XT as the test subject, 
# but can be used with any other device

# Developed by Sean Roe 

#! /usr/bin/env/python

import os,sys
from scapy.all import *

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

def wait():
    raw_input("Press Enter To Continue...")


menu = {}
menu['1']="Oversized Packet"
menu['2']="ICMP Flood"
menu['3']="SYN Flood"
menu['4']="UDP Flood"
menu['5']="Ping O' Death"
menu['6']="Teardrop Attack"
menu['7']="NMAP Port Scan"
menu['8']="ARP Spoof"
menu["x"]="Exit"

a=True
while a:

        clear()
	print("##############################")
	print("# Netscreen 5XT Testing Menu #")
	print("##############################")
	#clear
	options=menu.keys()
	options.sort()
    	for entry in options:
            print entry, menu[entry]
        
    	case=raw_input("Select script to run: ")
    	if case == '1':
	    print("##############################")
	    print("#      Large TCP Packet      #")
	    print("##############################")
            os.system('python /netscreen/large_packet.sca.py')
            wait()

    	elif case == '2':
            
	    print("##############################")
	    print("#         ICMP Flood         #")
	    print("##############################")
            os.system('python /netscreen/ICMP_flood_sca.py')
            wait()

    	elif case == '3':
	    print("###############################")
	    print("#          SYN Flood          #")
	    print("###############################")
            os.system('python /netscreen/SYN_flood_sca.py')
            wait()

	elif case == '4':
	    print("###############################")
	    print("#          UDP Flood          #")
	    print("###############################")
	    os.system('python /netscreen/UDP_flood_sca.py')
	    wait()

	elif case == '5':
	    print("###############################")
	    print("#        Ping of Death        #")
	    print("###############################")
	    os.system('python /netscreen/pingadeth_sca.py')
            wait()

        elif case == '6':
	    print("###############################")
	    print("#       Teardrop Attack       #")
	    print("###############################")
            os.system('python /netscreen/teardrop_sca.py')
            wait()
        
        elif case == '7':
	    print("################################")
	    print("#        NMAP Port Scan        #")
	    print("################################")
            os.system('python /netscreen/nmap_scan.py')
            wait()

        elif case == '8':
	    print("###############################")
	    print("#          ARP Spoof          #")
	    print("###############################")
            os.system('python /netscreen/arpspoof.py')
            wait()

    	elif case == "x":
            a=False
            clear()

    	else:
            print("Please select a valid option")
            wait()

        


