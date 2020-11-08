import os
import logo

def lvm_script_caller():
    os.system("clear")
    os.system('tput setaf 41')
    logo.main_menu()
    print("\n\n\t\t------------ Automated lvm -----------------\n\n")
    print("Make sure that you have spare storage to create a LVM")
    os.system("yum install lvm2")
    os.system("fdisk -l")
    drive_name=input("enter the name of the drive")
    os.system(f"pvcreate {drive_name} -ff")

    vgname=input("enter the name of the Volume group")
    os.system(f"vgcreate {vgname} {drive_name}")

    os.system("vgdisplay")

    size=input("Enter the size of drive you want in gigabytes ")
    name=input("What should be the name of the partition ")
    os.system(f"lvcreate --size {size}G --name {name} {vgname}")

    os.system(f"mkfs.ext4 /dev/{vgname}/{name}")

    mount_folder=input("enter the folder where you want to mount the storage ")
    os.system(f"mount /dev/{vgname}/{name} /{mount_folder}")

    os.system("df -h")
    input("Enter to continue")