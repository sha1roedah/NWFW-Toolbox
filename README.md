# NWFW-Toolbox
Collection of basic scripts to lightly harass a network firewall
- menu.py	
  - Main Menu
- ICMP_flood_sca.py	
  - Scapy script that sends 9001 ICMP packets to target IP address
- large_packet_sca.py	
  - Scapy script that sends a 60,000 byte packet to the target IP address on a random TCP port
- nmap_scan.py	
  - Python script that allows a user to enter in a target and variables for an NMAP scan
- pingadeth.py	
  - Scapy script that sends a 65,335 byte ICMP packet to target IP address
- SYN_flood_sca.py	
  - Scapy script that sends 9001 SYN packets to a random TCP port on target IP address
- UDP_flood_sca.py	
  - Scapy script that sends 15,000 UDP packets to a random UDP port on target IP address
- teardrop_sca.py	
  - Scapy script that forms packets with malformed offsets, causing a packet overlap
- Arpspoof.py	
  - Scapy script that spoofs the ARP tables of the gateway and the victim
