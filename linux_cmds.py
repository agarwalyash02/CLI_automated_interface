import os


def show_linux_command():
	print(""" 		Press 1 to check date
		 Press 2 to see calender
		 Press 3 to see Ram usage
		 Press 0 to exit
		 Press 9 for main menu""")

	linux_command = int(input())

	if linux_command == 1:
		date_show()
	elif linux_command == 2:
		show_calender()
	elif linux_command == 3:
		ram_usage()
	elif linux_command == 0:
		os.system('exit()')
	else:
		print("Invalid input plz retry")
		clear_screen_linux()

def clear_screen_linux():
	os.system('clear')
	show_linux_command()


def date_show():
	os.system('date')
def show_calender():
	os.system('cal')
def ram_usage():
	os.system('free -m')
