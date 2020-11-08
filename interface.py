import linux_cmds
import hadoop_setup
import linux_partition
import aws_cli
import getpass
import docker
import logo
import webserver
import yum
import os

def initial_interface():
	val = 0
	password = "team_18"
	while(True):
		os.system('clear')
		logo.main_menu()
		if int(val) == 0:
			print("Enter pass to continue : ")
			pas = getpass.getpass()
			if pas != password:
				print("incorrect password plz try again")
				input("Enter to continue")
				exit()
			val = 1

		num = 0
		print("\n\n")
		print("""		 
			Press 1 for performing Linux Command
		 	Press 2 for performing Hadoop Setup
		 	Press 3 for linux partitioining
		 	Press 4 for AWS CLI configuration for Windows
		 	Press 5 to use docker
		 	Press 6 to use webserver
		 	Press 7 to configure yum
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
			docker.load_docker_cmds()
		elif num == 6:
			webserver.load_webserver_cmds()
		elif num == 7:
			yum.load_yum_cmds()
		elif num == 0:
			print("Thanks for visiting")
			exit()
		else:
			print("Incorrect input please try again")
			input("Enter to continue")



initial_interface()