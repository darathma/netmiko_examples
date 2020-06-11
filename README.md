# netmiko_examples
Examples of using netmiko to Connect to Cisco IOS Devices

devices.txt - csv file for reading/listing multiple devices to be utilized by programs

show_version.py - simple program to connect to Cisco IOS devices and display the software version

multi_backup.py - program to backup the configration from multiple Cisco IOS devices to files

multi_config_changes.py - program to connect to multiple Cisco IOS devices and execute the configuration commands located in multi_config_changes.txt

multi_config_changes.txt - text file for listing configuration commands to be executed

lldp.py - program to connect to multiple Cisco IOS devices and find out if LLDP is enabled.  Write devices with LLDP enabled to an enabled file and the devices with LLDP disabled to a separate file.  Uses ExportDevice.csv for input. 
