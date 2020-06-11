from netmiko import ConnectHandler
import getpass
from datetime import date
import re

user = input('Enter your username: ')
password = getpass.getpass()
today = date.today()

device_list = []               ##create empty list named device_list

print('Reading CSV Input')
file = open('ExportDevice.csv',mode = 'r')		#open ExportDevice.csv in read-only mode
for line in file:			#read each line individually from devices.txt file
    device_info_list = line.strip().split(',')	#read each line into a list separated by “,”
    device_info = {}			#create empty dictionary named device_info
    print('------------------------------------------')
    print('Place', device_info_list[0], 'information into a dictionary named device_info:')
    print('------------------------------------------')
    device_info['host'] = device_info_list[0]	#for key “host”, assign it value in position 0 from device_info_list
    device_info['device_type'] = 'cisco_ios'
    device_info['ip'] = device_info_list[1]	 #for key “ip”, assign it value in position 1 from device_info_list…etc
    device_info['username'] = user           #for key "username", assign it variable user
    device_info['password'] = password       #for key "password", assign it variable password
    device_info['secret'] = password         #for key "secret", assign it variable password (could also create another variable to gather the secret)
    device_list.append(device_info)         #append dictionary to device_list

for device in device_list:
    net_connect = ConnectHandler(**device)
    net_connect.enable()
    net_connect.send_command('terminal length 0')
    hostname = device['host']
    print('Running commands on {}'.format(hostname))
    pattern_disabled = re.compile('LLDP is not enabled')
    pattern_enabled = re.compile('Status: Active', re.IGNORECASE)
    output = net_connect.send_command('show lldp')
    output_file_disabled = open('lldp_disabled_switches_{}.txt'.format(today), 'a')
    output_file_enabled = open('lldp_enabled_switches_{}.txt'.format(today), 'a')
    for line in output.splitlines():
        if pattern_disabled.search(line) != None:
            print('lldp is disabled on {}'.format(hostname))
            output_file_disabled.write('lldp is disabled on {}\n'.format(hostname))
        elif pattern_enabled.search(line) != None:
            print('lldp is enabled on {}'.format(hostname))
            output_file_enabled.write('lldp is enabled on {}\n'.format(hostname))
    
    output_file_disabled.close()
    output_file_enabled.close()
    net_connect.disconnect()