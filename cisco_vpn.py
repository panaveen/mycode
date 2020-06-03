#!/usr/bin/python3.6

from netmiko import ConnectHandler 
import os
import datetime

cisco_asa = {
     'device_type': 'cisco_asa',
     'host': 'fwmc0311-08.ent.mgmt.phx3.gdg',
     'username': 'nalagaraja',
     'password': 'Ccnp_rs12345',
     'secret': 'Ccnp_rs12345'
     }
net_connect = ConnectHandler(**cisco_asa)
output1 = net_connect.send_command("show vpn-sessiondb ra-ikev1-ipsec | i  Username")
output2 = net_connect.send_command("show vpn-sessiondb anyconnect | i Username")
now = datetime.datetime.now()
filename = os.path.join("/home/nalagaraja/scripts/", "output.txt")
with open(filename, "a") as f:
    print("Date and time : {}".format(now.ctime()), file=f)
    # print(now.strftime("%Y-%m-%d %H:%M:%S"), file=f)
    print(f"-------- Cisco VPN ---------", file=f) 
    print(f"--------- IPSEC ------------", file=f)
    print(output1, file=f)
    print(f"------- ANYCONNECT ---------", file=f)
    print(output2, file=f)
    print("--------- End ---------", file=f) 
