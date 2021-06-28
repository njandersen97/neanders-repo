import re
old_endpoint_list = ['10.1.1.1', '10.2.2.2']
#current_config_ips = ['10.1.1.1', '10.2.2.2']
new_tacacs_endpoint_list = ['10.3.3.3', '10.4.4.4']

# matched = (set(old_endpoint_list) == set(current_config_ips))
# if matched == True:
#     print("Greater Success")


# config_command_list = list()
# running_config = 'tacacs-server key 7 071C354D5C051807\ntacacs-server host 10.1.1.1 vrf MGMT\ntacacs-server host 10.2.2.2 vrf MGMT\naaa authentication login default group tacacs+ local\naaa authentication login console group tacacs+ local\naaa authentication enable default group tacacs+ local\naaa authorization exec default group tacacs+ local\naaa authorization commands all default group tacacs+ local\naaa accounting exec default start-stop group tacacs+\naaa accounting commands all default start-stop group tacacs+\nip tacacs source-interface Management0'
# old_endpoint_regex = r'tacacs-server host (\d+.\d+.\d+.\d+)'
# current_config_ips = re.findall(old_endpoint_regex, running_config)
# matched = (set(old_endpoint_list) == set(current_config_ips))
# if matched == True:
#     for ip in new_tacacs_endpoint_list:
#         config_command_list.append(f'tacacs-server host {ip} vrf MGMT')
#     print(config_command_list)
#     #self.connection.send_config_set(config_command_list)
#     #self.connection.send_command('copy run start')
#     #return True
# else:
#     #logging.error(f'Could not add new TACACs Endpoints to the device\n')
#     #return False

#set(sub_list).issubset(set(test_list))

running_config = 'tacacs-server key 7 071C354D5C051807\ntacacs-server host 10.1.1.1 vrf MGMT\ntacacs-server host 10.2.2.2 vrf MGMT\ntacacs-server host 10.3.3.3 vrf MGMT\ntacacs-server host 10.4.4.4 vrf MGMT\naaa authentication login default group tacacs+ local\naaa authentication login console group tacacs+ local\naaa authentication enable default group tacacs+ local\naaa authorization exec default group tacacs+ local\naaa authorization commands all default group tacacs+ local\naaa accounting exec default start-stop group tacacs+\naaa accounting commands all default start-stop group tacacs+\nip tacacs source-interface Management0'
current_endpoint_regex = r'tacacs-server host (\d+.\d+.\d+.\d+)'
current_config_ips = re.findall(current_endpoint_regex, running_config)
print(current_config_ips)
if set(old_endpoint_list).issubset(set(current_config_ips)) and set(new_tacacs_endpoint_list).issubset(set(current_config_ips)):
    config_command_list = []
    for ip in old_endpoint_list:
        config_command_list.append(f'no tacacs-server {ip}')
    print(config_command_list)
    #self.connection.send_config_set(config_commands)
    #self.connection.send_command('copy run start')
    #return True
else:
    print('fail')
    #logging.error(f'No given TACACs Endpoints did not match what the device had\n')
    #return False


















