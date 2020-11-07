import linux_cmds
import hadoop_setup
import linux_partition
import aws_cli
import getpass
import os

def main_menu():
	print("""
	         _______________________
         	|                       |
         	|One-For-All Interface  |
         	|_______________________|
         	""")


def initial_interface():
	val = 0
	password = "team_18"
	while(True):
		os.system('clear')
		main_menu()
		if int(val) == 0:
			print("Enter pass to continue : ")
			pas = getpass.getpass()
			if pas != password:
				print("incorrect password plz try again")
				input("Enter to continue")
				exit()
			val = 1
			
		num = 0
		print("\n\n\n\n")
		print("""		 
			Press 1 for performing Linux Command
		 	Press 2 for performing Hadoop Setup
		 	Press 3 for linux partitioining
		 	Press 4 for AWS CLI configuration for Windows
		 	Press 5 to use docker
		 	Press 0 to exit""")
		num = int(input("Enter your choice: "))

		if num == 1:
			linux_cmds.show_linux_command()
		elif num == 2:
			hadoop_setup.load_hadoop()
		elif num == 3:
			linux_partition.load_partition()
		elif num == 4:
			aws_cli.load_cmds_aws()
		elif num == 5:
			pass
		elif num == 0:
			print("Thanks for visiting")
			exit()
		else:
			print("Incorrect input please try again")
			input("Enter to continue")



initial_interface()