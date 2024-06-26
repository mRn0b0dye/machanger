#!/usr/bin/env python

from time import sleep
import subprocess as sub
import optparse
import re
import os
import random
import sys

def help_menu():
    usage = 'python3 {} [-i <interface> -m <newmac>] [--anonymus-mode <interface>] [--random-mac <interface>] [-s <interface>]'.format(sys.argv[0])
    arg = optparse.OptionParser(usage= usage)
    arg.add_option("-i", "--interface", dest= "interface", help= "Select Interface")
    arg.add_option("-m", "--macaddr", dest= "new_mac", help= "New Mac Address *Use sudo*")
    arg.add_option("-s", "--show-mac", dest= "interface", help= "Mac Address")    
    arg.add_option("-a", "--anonymus-mode", dest= "interface", help= "generate a random mac address and change continously *Use sudo*")
    arg.add_option("-r", "--random-mac", dest= "interface", help= "generating random mac address *Use sudo*")
    (options, arguments) = arg.parse_args()
    return options

def generate_random_mac():
    mac_bytes = ["00"]
    for _ in range(5):
      mac_bytes.append(f"{random.randint(0, 255):02x}")
    mac_bytes[0] = f"{int(mac_bytes[0], 16) | 0x2:02x}"
    return ":".join(mac_bytes)

def setting_random_mac(interface):
    random_mac = generate_random_mac()
    mac_addr_current = check_mac(interface)
    print(f'\033[0;31mCurrent Mac Address: {mac_addr_current}\033[0m')
    sub.call(['ifconfig', interface, "down"])
    sub.call(['ifconfig', interface, "hw", "ether", random_mac])
    sub.call(['ifconfig', interface, "up"])
    print(f'\033[0;31mNew Mac Address: {random_mac}\033[0m')    

def going_to_be_anonymus(interface):
    while True:
        random_mac = generate_random_mac()
        mac_addr_current = check_mac(interface)
        print(f'\033[0;35mCurrent Mac Address: {mac_addr_current}\033[0m')
        sub.call(['ifconfig', interface, "hw", "ether", random_mac])
        print(f'\033[0;35mNew Mac Address: {random_mac}\033[0m\n')
        sleep(4)

def macchanger(interface, new_mac):
    mac_addr_current = check_mac(interface)
    sub.call(['ifconfig', interface, "down"])
    sub.call(['ifconfig', interface, "hw", "ether", new_mac])
    sub.call(['ifconfig', interface, "up"])
    print(f'\033[1;35mCurrent Mac: {mac_addr_current}\033[0m')
    print(f'\033[1;35mNew Mac: {new_mac}\033[0m')

def check_mac(interface):
    mac_addr_raw = sub.check_output(['ifconfig',interface])
    mac_addr_current = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', str(mac_addr_raw))
    return mac_addr_current.group(0)

def main():
    try:
        if ( sys.argv[1] == '-i' or sys.argv[1] == '--interface' ) and ( sys.argv[3] == '-m' or sys.argv[3] == '--macaddr' ):
            macchanger(options.interface, options.new_mac)
            exit()
        elif ( sys.argv[1] == '-a' or sys.argv[1] == '--anonymus-mode' ):
            going_to_be_anonymus(options.interface)
            exit()
        elif ( sys.argv[1] == '-s' or sys.argv[1] == '--show-mac' ):
            print('\033[1;33m{}\033[0m'.format(check_mac(options.interface)))
            exit()
        elif ( sys.argv[1] == '-r' or sys.argv[1] == '--random-mac' ):
            setting_random_mac(options.interface)
    except KeyboardInterrupt:
        print("\n\033[1;33m[*]\033[0m \033[1;31mExiting program...\033[0m")
        sys.exit()
    except IndexError:
        print("\033[1;31mUse -h or --help for help\033[0m")


if __name__ == "__main__":
    if os.getuid() != 0:
        print("\033[1;31m{}\033[0m \033[0;31mrequires sudo privileges to run.\033[0m".format(sys.argv[0]))
        exit()
    options = help_menu()
    main()
