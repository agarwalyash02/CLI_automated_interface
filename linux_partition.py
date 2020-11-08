import os
import logo

def load_partition():
	while True:
		os.system('clear')
		logo.main_menu()
		print('''
			What you want to do in partition !!
			1. create a partition
			2. format a partition
			3. mount a partition
			9. return to main menu
			''')
		hadoop_input = input("Enter here: ")
		hadoop_input = int(hadoop_input)

		if hadoop_input == 1:
			create_partition()
		elif hadoop_input == 2:
			format_partition()
		elif hadoop_input == 3:
			mount_partition()
		elif hadoop_input == 9:
			break
		else:
			print("Incorrect input please try again")
			input("Enter to continue")


def create_partition():
	print("\n\nBelow are the available disk: \n\n")
	os.system('fdisk -l')
	disk_name = input("Enter name of disk you want to make partition: ")
	print("\n\nAfter this you have to mannualy make partition\n\n")
	os.system('fdisk {}'.format(disk_name))

def format_partition():
	print("\n\nBelow are the available disk with partition: \n\n")
	os.system('fdisk -l')
	partition_name = input("Enter name of partition you want to format: ")
	os.system('mkfs.ext4 {}'.format(partition_name))

def mount_partition():
	val = input("\t1. if folder is already created\n\t2. to created a new folder\n\t Enter your choice: ")
	fol_name = "temp"
	if int(val) == 1:
		fol_name = input("Enter the name of folder with location: ")
	elif int(val) == 2:
		fol_name = input("Enter the name of folder you want to create with location where to create: ")
		os.system('mkdir {}'.format(fol_name))
		print("\n\nBelow are the available disk with partition: \n\n")
		os.system('fdisk -l')
		partition_name = input("\n\nEnter name of partition you want to format: ")
		os.system('mount {} {}'.format(partition_name,fol_name))


