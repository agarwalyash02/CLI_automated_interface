import os


def load_hadoop():
	while True:
		os.system('clear')
		print('''
			What you want to do in hadoop !!
			1. setup the hdfc-site file
			2. setup the core-site file
			3. start the service of datanode
			4. start the service of namenode
			5. check the dfsadmin report
			6. Upload a file from client
			7. List all the file present in the cluster for namenode and client
			9. return to main menu
			''')
		hadoop_input = input("Enter here: ")
		hadoop_input = int(hadoop_input)

		if hadoop_input == 1:
			setup_hdfs()
		elif hadoop_input == 2:
			setup_core()
		elif hadoop_input == 3:
			start_datanode()
		elif hadoop_input == 4:
			start_namenode()
		elif hadoop_input == 5:
			check_report()
		elif hadoop_input == 6:
			upload_file_client()
		elif hadoop_input == 7:
			list_file()
		elif hadoop_input == 9:
			break
		else:
			print("Incorrect input please try again")
			input("Enter to continue")




def setup_hdfs():
	os.system('clear')
	val=input('''For configuring hdfs file . 
			1. for namenode 
			2. for datanode
			3. for client
			Enter here: ''')
	val = int(val)

	if val == 1:
		con_hdfs_namenode()
	elif val == 2:
		con_hdfs_datanode()
	elif val == 3:
		con_hdfs_client()

def setup_core():
	os.system('clear')
	val = input('''For configuring core-site file .
				1. for namenode
				2. for datanode or client : 
				Enter here: ''')
	if int(val) == 1:
		con_core_namenode()
	elif int(val) == 2:
		con_core_client_datanode()

def start_datanode():
	os.system('hadoop-daemon.sh start datanode')

def start_namenode():
	os.system('hadoop-daemon.sh start namenode')

def check_report():
	os.system('clear')
	report = os.system('hadoop dfsadmin -report')
	print(report)
	input("Enter to continue: ")

def upload_file_client():
	os.system('clear')
	file_name = input("Enter the name of file with location : ")
	os.system('hadoop fs -put {} /'.format(file_name))

def list_file():
	os.system('clear')
	print(os.system('hadoop fs -ls /'))
	input("Enter to continue")




def con_core_namenode():
	port = input("Enter the port no on which you want to run hadoop services: ")
	with open("/etc/hadoop/core-site.xml",'w+') as f:
		f.write("<?xml version='1.0'?>\n")
		f.write("<?xml-stylesheet type='text/xsl' href='configuration.xsl'?>\n\n")
		f.write("<!-- Put site-specific property overrides in this file. -->\n\n")
		f.write("<configuration>\n")
		f.write("<property>\n")
		f.write("<name>fs.default.name</name>\n")
		f.write("<value>hdfs://0.0.0.0:{}</value>\n".format(int(port)))
		f.write("</property>\n")
		f.write("</configuration>\n")

def con_core_client_datanode():
	port = input("Enter the port no. on which hadoop services is running in namenode: ")
	ip_name = input("Enter the ip of namenode")
	with open("/etc/hadoop/core-site.xml",'w+') as f:
		f.write("<?xml version='1.0'?>\n")
		f.write("<?xml-stylesheet type='text/xsl' href='configuration.xsl'?>\n\n")
		f.write("<!-- Put site-specific property overrides in this file. -->\n\n")
		f.write("<configuration>\n")
		f.write("<property>\n")
		f.write("<name>fs.default.name</name>\n")
		f.write("<value>hdfs://{}:{}</value>\n".format(ip_name,int(port)))
		f.write("</property>\n")
		f.write("</configuration>\n")

def con_hdfs_namenode():
	answer = input('''For configuring we have to create a folder
				1. folder already created in this we will format the existing folder
				2. to create a new folder
				Enter here: ''')
	dir_name = input("Give the name of the folder want to create or already exist: ")
	if int(answer) == 2:
		os.system("mkdir /{}".format(dir_name))
	os.system('hadoop namenode -format ')

	with open("/etc/hadoop/hdfs-site.xml",'w+') as f:
		f.write("<?xml version='1.0'?>\n")
		f.write("<?xml-stylesheet type='text/xsl' href='configuration.xsl'?>\n\n")
		f.write("<!-- Put site-specific property overrides in this file. -->\n\n")
		f.write("<configuration>\n")
		f.write("<property>\n")
		f.write("<name>dfs.name.dir</name>\n")
		f.write("<value>/{}</value>\n".format(dir_name))
		f.write("</property>\n")
		f.write("</configuration>\n")

def con_hdfs_datanode():
	answer = input('''For configuring we have to create a folder
				1. folder already created in this we will delete the existing folder and create new folder
				2. to create a new folder
				Enter here: ''')
	dir_name = input("Give the name of the folder want to create or already exist : ")
	if int(answer) == 2:
		os.system("mkdir /{}".format(dir_name))
	elif int(answer)==1:
		os.system("rm -rf /{}".format(dir_name))
		os.system("mkdir /{}".format(dir_name))

	with open("/etc/hadoop/hdfs-site.xml",'w+') as f:
		f.write("<?xml version='1.0'?>\n")
		f.write("<?xml-stylesheet type='text/xsl' href='configuration.xsl'?>\n\n")
		f.write("<!-- Put site-specific property overrides in this file. -->\n\n")
		f.write("<configuration>\n")
		f.write("<property>\n")
		f.write("<name>dfs.data.dir</name>\n")
		f.write("<value>/{}</value>".format(dir_name))
		f.write("</property>\n")
		f.write("</configuration>\n")

def con_hdfs_client():
	answer=input('''default replication factor of haddop is 3 and default block size is 64Mb
				1. to exit without change
				2. to change replication factor and block size
				Enter here: ''')

	if int(answer) ==1:
		return
	rep = input("Enter the new replication factor: ")
	block = input("Enter the new block size min block size is 1Mb: ")
	if int(block) < 1:
		print("incorrent input try again")
		con_hdfs_client()
	with open("/etc/hadoop/hdfs-site.xml",'w+') as f:
		f.write("<?xml version='1.0'?>\n")
		f.write("<?xml-stylesheet type='text/xsl' href='configuration.xsl'?>\n\n")
		f.write("<!-- Put site-specific property overrides in this file. -->\n\n")
		f.write("<configuration>\n")
		f.write("<property>\n")
		f.write("<name>dfs.replication</name>\n")
		f.write("<value>{}</value>\n".format(int(rep)))
		f.write("</property>\n\n")
		f.write("<property>\n")
		f.write("<name>dfs.block.size</name>\n")
		f.write("<value>{}</value>\n".format(int(block)))
		f.write("</property>\n")
		f.write("</configuration>\n")
        