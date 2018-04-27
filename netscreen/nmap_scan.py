import os, sys

targetIP=raw_input("Target IP Address: ")
flags=raw_input("NMAP Flags (optional): ")

os.system('nmap '+targetIP+' '+flags)
