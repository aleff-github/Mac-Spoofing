from os import system
from termcolor import colored
import pyfiglet


def get_info():
	print( colored("[+] ifconfig", "green"), end="\n\n\n")
	system("ifconfig -a")
	print("\n")
	
def get_interface_name():
	get_info()
	print(colored("[+] If you have something like ", "green") + "\"eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500\"" + colored("your interface name is ", "green") + "eth0", end="\n\n\n")
	input_interface()

def input_interface():
	choose = input(colored("[?] Do you know your interface name? [Y/N] ", "green"))

	if "N" in choose:
		get_interface_name()
	else:
		return input(colored("[+] Insert your interface name: ", "green"))
		
def get_fake_mac():
	choose = input(colored("[?] Do you want insert a specific Mac Address? [Y/N] ", "green"))
	if "Y" in choose:
		return input(colored("[+] Insert your Mac Address: ", "green"))
	else:
		return "00:aa:11:bb:22:cc"
	
def get_new_info():
	choose = input(colored("[?] Do you want to see you new Mac Address? [Y/N] ", "green"))
	if "Y" in choose:
		get_info()
		
def mac_spoofing(interface, mac_addr):
	print(colored("[+] Loading...", "green"))
	system("ifconfig {} down".format(interface))
	system("ifconfig {} hw ether {}".format(interface, mac_addr))
	system("ifconfig {} up".format(interface))
	print(colored("[+] If the Mac Addres is not changed please retry with an another one.", "green"))
	get_info()

def main():
	system("clear")
	pyfiglet.figlet_format("NoNameoN", font="slant")
	interface = input_interface()
	mac_addr = get_fake_mac()
	mac_spoofing(interface, mac_addr)

main()
