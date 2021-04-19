from os import system

interface = input("Insert your interface name: ")
mac_addr = input("Insert new Mac Address: ")

print("[+] Loading...")

system("ifconfig {} down".format(interface))
system("ifconfig {} hw ether {}".format(interface, mac_addr))
system("ifconfig {} up".format(interface))

print("[+] Mac Address changed!")
