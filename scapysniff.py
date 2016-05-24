#!/usr/bin/python

# scapysniff.py

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

from scapy.all import *
import sys

if len(sys.argv) != 2:
    print("usage: scapysniff.py <interface>")
    sys.exit(1)
 
interface = sys.argv[1]

pkts = sniff(iface=interface, prn=lambda x:x.summary())


