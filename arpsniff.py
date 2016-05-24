#!/usr/bin/python

# arpsniff.py

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

from scapy.all import *
import sys

if len(sys.argv) != 2:
    print("usage: arpsniff.py <interface>")
    sys.exit(1)

interface = sys.argv[1]

def callback(pkt):
    if ARP in pkt and pkt[ARP].op in (1,2):
        return pkt.sprintf("%ARP.hwsrc% %ARP.psrc%")


pkts = sniff(iface=interface, prn=callback, filter="arp", store=0)




