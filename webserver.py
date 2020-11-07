#!/usr/bin/python3
import os

print("""
Configuration of Apache httpd web server !! 
press 1 for configuring httpd server
press 2 for removing httpd server
press 3 for exit
""")
n=int(input("Enter your choice!! \n"))

if n==1:
	while True:	
		print("""
		Select your options:
		1.To install httpd server
		2.To setup webserver
		3.To start web server
		4.To stop web server
		5.To check status of web server
		6.To exit  \n
		""")
		ch=input()
		if int(ch)==1:
			os.system("yum install httpd")
		elif int(ch)==2:
			i=input("Enter your file name \n")
			os.system("vi /var/www/html/{}.html".format(i))
		elif int(ch)==3:
			os.system("systemctl start httpd")
		elif int(ch)==4:
			os.system("systemctl stop httpd")
		elif int(ch)==5:
			os.system("systemctl status httpd")
		elif int(ch)==6:
			exit()		
		else :
			print("Invalid choice!\n")

elif n==2:
	os.system("yum remove httpd")

else :
	exit()

