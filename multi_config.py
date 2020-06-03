from netmiko import ConnectHandler
import getpass

user = input('Enter your username: ')
password = getpass.getpass()

print('Reading CSV Input')
device_list = []               ##create empty list named device_list
file = open('devices.txt',mode = 'r')		#open devices.txt in read-only mode
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
    output = net_connect.send_config_from_file('multi_config_changes.txt')
    print(output)
    net_connect.save_config()
    net_connect.disconnect()
