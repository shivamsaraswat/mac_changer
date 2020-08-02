"""Description: This program is used to securely modify the MAC Address of the desired network interface (MAC Address Changer)"""
print(__doc__+"\n")

import optparse  # OptParse is a module introduced in Python that makes it easy to write command line tools
import re   # This module is used to do matching operations
import subprocess  # Subprocess is a module used to deal with Terminal (command line) commands


def get_arguments():
    # creating an OptionParser instance
    parser = optparse.OptionParser("mac_changer.py [options]")
    # defining options
    parser.add_option("-i", "--interface", dest = "interface", help = "Interface to change its MAC Address")
    parser.add_option("-m", "--mac", dest = "new_mac", help = "New MAC Address")
    # instructing optparse to parse program command line
    (options, arguments) = parser.parse_args()  # options contains values, arguments contains fixed arguments
    # Checking if user is not giving proper inputs
    if not options.interface:
        parser.error("[-] Please specify an interface, use -h or --help for more info")
    elif not options.new_mac:
        parser.error("[-] Please specify a new mac, use -h or --help for more info")
    return options

def change_mac(interface, new_mac): # Changing MAC Address
    # subprocess.call is used to run the command described by given arguments
    subprocess.call(["ifconfig", interface, "down"])    
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    print("[+] Changing MAC Address for " + interface + " to " +  new_mac)

def get_current_mac(interface):
    # subprocess.check_output is used run command with arguments and return its output
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    # finding MAC from the output of ifconfig command
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        return "[-] Could not find MAC Address"

options = get_arguments()                           # passing arguments

current_mac = get_current_mac(options.interface)    # getting old MAC
print("Current MAC Address = " + str(current_mac))  # printing current MAC

change_mac(options.interface, options.new_mac)      # changing MAC

current_mac = get_current_mac(options.interface)    # getting updated MAC

if current_mac == options.new_mac:                  # changing if MAC changed as per user requirement
    print("[+] MAC Address was successfully changed to " + current_mac)
else:
    print("[-] MAC Address did not changed")
