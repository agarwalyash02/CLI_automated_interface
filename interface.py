import linux_cmds

print("""          _______________________
         |                       |
         |One-For-All Interface  |
         |_______________________|                   """)


def initial_interface():
	print("\n\n\n\n")
	print("""		 Press 1 for performing Linux Command
		 Press 2 for performing Hadoop Setup
		 Press 3 for partitioining
		 Press 4 for AWS CLI configuration
		 Press 5 to use docker
		 Press 0 to exit""")
	num = int(input())

	while num!=0:
		if num == 1:
			linux_cmds.clear_screen_linux()
		'''elif num == 3:'''


def clear_screen_interface():
	os.system('clear')
	initial_interface()

initial_interface()