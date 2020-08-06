from netmiko import ConnectHandler

username = input('Username: ')
password = input('Password: ')

device_name_file = open('device_name.txt')
device_name = device_name_file.read().splitlines()

device_dict = {
    'host': device_name,
    'username': username,
    'password': password,
    'device_type': 'arista_eos'

}

cfg_file = "config_changes.txt"
with ConnectHandler(**device_dict) as net_connect:
    output = net_connect.send_config_from_file(cfg_file)
    output += net_connect.save_config()

print()
print(output)
print()