import linux_cmds
import hadoop_setup
print("""          _______________________
         |                       |
         |One-For-All Interface  |
         |_______________________|                   """)


def initial_interface():
	while(True):
		os.system('clear')
		num = 0
		print("\n\n\n\n")
		print("""		 Press 1 for performing Linux Command
		 	Press 2 for performing Hadoop Setup
		 	Press 3 for partitioining
		 	Press 4 for AWS CLI configuration
		 	Press 5 to use docker
		 	Press 0 to exit""")
		num = int(input())

			if num == 1:
				linux_cmds.clear_screen_linux()
			elif num == 2:
				hadoop_setup.load_hadoop()
			elif num == 3:
				pass
			elif num == 4:
				pass
			elif num == 5:
				pass
			elif num == 0:
				print("Thanks for visiting")
				exit()
			'''elif num == 3:'''


def clear_screen_interface():
	os.system('clear')
	initial_interface()

initial_interface()