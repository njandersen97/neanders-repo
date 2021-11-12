# This script is to experiment with the "expect_string" parameter of the send_command for Netmiko
from netmiko import ConnectHandler
from getpass import getpass

import logging

logging.basicConfig(filename="disable.log", level=logging.DEBUG)
logger = logging.getLogger("netmiko")

my_device = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
}

net_connect = ConnectHandler(**my_device)

print(net_connect.find_prompt())
# When you send the "disable" command on IOS, you drop out of the enable prompt, going form cisco3# to cisco3>
output = net_connect.send_command("disable", expect_string=r">")
print(output)
print(net_connect.find_prompt())
net_connect.disconnect()
