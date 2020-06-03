from netmiko import ConnectHandler
import getpass

user = input('Enter your username: ')
password = getpass.getpass()


izzy_swi = {
    'device_type': 'cisco_ios',
    'ip': '10.1.2.11',
    'username': user,
    'password': password,
    'secret': password,
}

willie_swi = {
    'device_type': 'cisco_ios',
    'ip': '10.1.2.12',
    'username': user,
    'password': password,
    'secret': password,
}

devices = [izzy_swi, willie_swi]

for device in devices:
    net_connect = ConnectHandler(**device)
    net_connect.enable()
    output = net_connect.send_command('show version')
    print(output)
    net_connect.disconnect()