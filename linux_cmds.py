import os

def show_linux_command():
	while True:
		os.system('clear')
		print(""" 		
			Press 1 to check date
			Press 2 to see calender
			Press 3 to see Ram usage
			Press 9 return to main menu
			""")

		linux_command = int(input("Enter your choice here: "))

		if linux_command == 1:
			date_show()
		elif linux_command == 2:
			show_calender()
		elif linux_command == 3:
			ram_usage()
		elif linux_command == 9:
			break
		else:
			print("Incorrect input please try again")
			input("Enter to continue")


def date_show():
	os.system('date')
def show_calender():
	os.system('cal')
def ram_usage():
	os.system('free -m')
