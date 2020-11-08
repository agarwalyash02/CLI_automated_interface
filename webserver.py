import os
import logo

def load_webserver_cmds():
	while True:	
		os.system("clear")
		logo.main_menu()
		ch = input("""
		Select your options:
		1. for writing a code in html file to host
		2. Service commmands to start, stop and get status of process
		9. return to main menu \n
		Enter your choice here: """)
		if int(ch)==1:
			setup_webserver()
		elif int(ch)==2:
			webserver_service_commands()
		elif int(ch)==9:
			break		
		else :
			print("Incorrect input please try again")
			input("Enter to continue")

def setup_webserver():
	os.system("clear")
	logo.main_menu()
	i=input("Enter your file name: ")
	print("Write a code in the file which gets open and save it we will host it")
	input("Enter to continue")
	os.system("vi /var/www/html/{}.html".format(i))


def webserver_service_commands():
    os.system("clear")
    logo.main_menu()
    cmd = input('''\n\nEnter the service commands:
        1. to start the httpd service
        2. to stop the httpd service
        3. to check the status of httpd service
        Enter your choice here: ''')
    service = "status"
    if int(cmd) == 1:
        service = "start"
    elif int(cmd) == 2:
        service = "stop"
    print(os.system('systemctl {} httpd'.format(service)))
    input("Enter to continue")