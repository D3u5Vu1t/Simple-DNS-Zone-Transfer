#!/bin/python3 

import dns.resolver
import dns.zone

def getDomain():
        domain = input("Enter a valid domain: ")
        return domain

def zone_xfr():

        while True:
                try:
                        domain = getDomain()
                        answers = dns.resolver.resolve(domain, 'NS')
                except Exception as e:
                        print ("[*] {} is an invalid domain, try again".format(domain))
                        continue
                break

        for rdata in answers:
                ip_data = dns.resolver.resolve(rdata.target, 'A')
                for ip in ip_data:
                        print ("[*] Found Server: NS {} and IP {}".format(rdata, ip))
                        try: 
                                zone = dns.zone.from_xfr(dns.query.xfr(str(ip), domain))
                                for host in zone: 
                                        print("[*] Found Host: {}".format(host))
                        except Exception as e:
                                print ("[*] {} refused zone transfer".format(rdata))

zone_xfr()
