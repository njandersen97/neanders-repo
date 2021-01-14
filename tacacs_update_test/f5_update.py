show_run_tacacs_secret = 'show running-config auth tacacs system-auth secret'

def update_tacacs_key
	running_config = self.connection.send_command(show_run_tacacs_secret)
	#Probably not working regex, placeholder
	tacacs_regex = r'.*(tacacsAction)\s+(?P<ActionName>\S+)\s+'
	updated = False
	
	#No idea if these work, just copied/modified
	for line in running_config.split('\n')
		match = re.search(tacacs_regex, line.strip())
		
		if match:
			config_commands = [
				'modify auth tacacs system-auth secret {key}'.format(key=new_key)}
	
			output = self.send_full_command(cmd)
                if 'error' in output:
                    return False
                else:
                    updated = True
				self.connection.send_command(save sys config)
				
			
	return updated
				