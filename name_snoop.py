#!/usr/bin/python

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
import sys

if len(sys.argv) != 3:
    print "\n\n             *** DNS-SNOOP ***          "
    print "   *** Justin Hutchens (HackitHutch) ***          "
    print "To perform DNS Cache Snooping on a target DNS Server\n"
    print "Usage - ./dns_snoop.py [DNS Server] [Domain List]"
    print "----------"
    print "Example - ./dns_snoop.py ns1.example.com domain_list.txt"
    print "Example will snoop the DNS cache of the ns1.example.com DNS server looking for domains in the domain_list.txt file"
    print "----------\n"
    sys.exit()
                                    
##Assigning System Arguments to script variables
dns_server = str(sys.argv[1])
domain_list = open(str(sys.argv[2]),'r')
print "Cached DNS Queries:\n"                                    
                                    
for domain in domain_list:
    dns_snoop = sr1(IP(dst=dns_server)/UDP(dport=53)/DNS(rd=0,qd=DNSQR(qname=domain.strip())),verbose=0,timeout=1)
    if dns_snoop[DNS].an == None:
        pass
    else:
        print dns_snoop[DNS].an[DNSRR].rrname + ' : ' + dns_snoop[DNS].an[DNSRR].rdata
