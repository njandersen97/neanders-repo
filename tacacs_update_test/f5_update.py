CMD_SHOW_TACACS_SECRET = 'show running-config auth tacacs system-auth secret'


@read_write_command
def update_tacacs_key(self, new_key):
	running_config = self.connection.send_command(self.CMD_SHOW_TACACS_SECRET)
	tacacs_regex = r'secret\s+(?P<key>.*)'
	for line in running_config.split('\n'):
		match = re.search(tacacs_regex, line.strip())
		if match:
			cmd = [
				'modify auth tacacs system-auth secret {}'.format(new_key)
			]
			self.connection.send_config_set(cmd)
			self.connection.send_command(self.CMD_SAVE_CONFIG)
			return True
	return False

