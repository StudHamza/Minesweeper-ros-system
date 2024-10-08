# autopep8: off
import os
import sys

sys.path.append(os.getcwd())

import lib.settings as set_man
# autopep8: on


settings_obj = set_man.get_settings()
raspi_ip = settings_obj['networking']['raspi']
raspi_ssh_username = settings_obj['security']['raspi']['username']
raspi_ssh_pass = settings_obj['security']['raspi']['password']

os.system(f'sshpass -p "{raspi_ssh_pass}" ssh {raspi_ssh_username}@{raspi_ip}')
