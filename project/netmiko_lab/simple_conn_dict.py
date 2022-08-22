from netmiko import ConnectHandler
from getpass import getpass

# Set up a dictionary for the device. The keys must match the required args
# for the handler
my_device = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
}

# The ** means you're not gonna pass in the dictionary as a single dict to
# connect handler, instead as separate arguments
net_connect = ConnectHandler(**my_device)
print(net_connect.find_prompt())
