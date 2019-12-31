# mac_changer.py
#Supports only Python 2 and applicable for Linux only

Description: This program is used to modify the MAC Address of the desired network interface (MAC Address Changer)

Usage: mac_changer.py [options]

Options:

    -h, --help            show this help message and exit
    -i INTERFACE, --interface=INTERFACE
                          Interface to change its MAC Address (interface like eth0, wlan0, etc.)
    -m NEW_MAC, --mac=NEW_MAC
                          New MAC Address
