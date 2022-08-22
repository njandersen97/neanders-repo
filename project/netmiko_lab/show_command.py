from netmiko import ConnectHandler
from getpass import getpass

my_device = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
}

net_connect = ConnectHandler(**my_device)

output = net_connect.send_command("show ip int br")
print(output)
net_connect.disconnect()
