from netmiko import ConnectHandler
from getpass import getpass

import logging

logging.basicConfig(filename='arp.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")

# Since all lab devices share the same password, I prompt the user for the password at the begining of the script
password = getpass()

arista1 = {
    "device_type": "arista_eos",
    "host": "arista1.lasthop.io",
    "username": "pyclass",
    "password": password,
}

arista2 = {
    "device_type": "arista_eos",
    "host": "arista2.lasthop.io",
    "username": "pyclass",
    "password": password,
}

arista3 = {
    "device_type": "arista_eos",
    "host": "arista3.lasthop.io",
    "username": "pyclass",
    "password": password,
}

arista4 = {
    "device_type": "arista_eos",
    "host": "arista4.lasthop.io",
    "username": "pyclass",
    "password": password,
}

for device in (arista1, arista2, arista3, arista4):
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command("show ip arp")
    # Display the hostname before showing the output
    print(device["host"])
    print(output)
    net_connect.disconnect()