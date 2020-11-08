import os
import logo
def show_linux_command():
	os.system('clear')
	os.system('tput setaf 41')
	logo.main_menu()
	print("\n\n\t\t------------ linux -----------------\n\n")
	val =input("""
		1. To run command locally
		2. To run command remotely we use ssh protocol
		Enter your choice here: """)
	req = dict()
	if int(val) == 2:
		req['ip_of_remote'] = input("Enter the ip of remote system : ")
	while True:
		os.system('clear')
		os.system('tput setaf 41')
		logo.main_menu()
		print("""\n\n\t\t------------ linux -----------------\n\n	
			Press 0 to check date
			Press 1 to see calender
			Press 2 to see Ram usage
			Press 3 to see the background running process
			Press 4 to check the ip address
			Press 5 to check from which we login
			Press 6 to start the firewall
			Press 7 to stop the firewall
			Press 8 to see about the CPU
			Press 9 to return to main menu
			""")

		linux_command = int(input("Enter your choice here: "))

		if linux_command == 0:
			date_show(val,req)
		elif linux_command == 1:
			show_calender(val,req)
		elif linux_command == 2:
			ram_usage(val,req)
		elif linux_command == 3:
			running_process(val,req)
		elif linux_command == 4:
			ip_address(val,req)
		elif linux_command == 5:
			who_am_i(val,req)
		elif linux_command == 6:
			firewall_start(val,req)
		elif linux_command == 7:
			firewall_stop(val,req)
		elif linux_command == 8:
			lscpu(val,req)
		elif linux_command == 9:
			break
		else:
			print("Incorrect input please try again")
			input("Enter to continue")


def date_show(val,req):
	if int(val) == 2:
		os.system('ssh {} date'.format(req['ip_of_remote']))
	else:
		os.system('date')
	input("Enter to continue")

def show_calender(val,req):
	if int(val) == 2:
		os.system('ssh {} cal'.format(req['ip_of_remote']))
	else:
		os.system('cal')
	input("Enter to continue")

def ram_usage(val,req):
	if int(val) == 2:
		os.system('ssh {} free -m'.format(req['ip_of_remote']))
	else:
		os.system('free -m')
	input("Enter to continue")
    
def running_process(val,req):
	if int(val) == 2:
		os.system('ssh {} jobs'.format(req['ip_of_remote']))
	else:
		os.system('jobs')
	input("Enter to continue")

def ip_address(val,req):
	if int(val) == 2:
		os.system('ssh {} ifconfig enp0s3'.format(req['ip_of_remote']))
	else:
		os.system('ifconfig enp0s3')
	input("Enter to continue")
    
def who_am_i(val,req):
	if int(val) == 2:
		os.system('ssh {} whoami'.format(req['ip_of_remote']))
	else:
		os.system('whoami')
	input("Enter to continue")
    
def firewall_start():
	if int(val) == 2:
		os.system('ssh {} systemctl start firewalld'.format(req['ip_of_remote']))
	else:
		os.system('systemctl start firewalld')
	input("Enter to continue")
    
def firewall_stop(val,req):
	if int(val) == 2:
		os.system('ssh {} systemctl stop firewalld'.format(req['ip_of_remote']))
	else:
		os.system('systemctl stop firewalld')
	input("Enter to continue")
    
def lscpu(val,req):
	if int(val) == 2:
		os.system('ssh {} lscpu'.format(req['ip_of_remote']))
	else:
		os.system('lscpu')
	input("Enter to continue")