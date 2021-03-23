import os

with open('ip_addresses.txt') as addresses:
    for ip_Add in addresses:
        os.system("echo Agent_Address = {}".format(ip_Add))
        os.system("c:/usr/bin/snmpwalk -v 2c -c public {}	1.3.6.1.4.1.5961.5.1".format(ip_Add))
        os.system("echo -------")
