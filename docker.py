import os
import logo

def load_docker_cmds():
    while True:
        os.system("clear")
        os.system('tput setaf 41')
        logo.main_menu()
        print("""\n\n\t\t------------ Automated docker -----------------\n\n
            1. Service commmands to start, stop and get status of process
            2. See current running containers
            3. View all containers
            4. Create a new Container
            5. Attach a running container
            9. return to main menu
        """)
        docker_c=input("Enter your choice here: ")

    
        if int(docker_c) == 1:
            docker_service_commands()
        elif int(docker_c)==2:
            view_instance()
        elif int(docker_c) == 3:
            view_all_instance()
        elif int(docker_c) == 4:
            create_container()
        elif int(docker_c) == 5:
            attach_container()
        elif int(docker_c) == 9:
            break
        else:
            print("Incorrect input please try again")
            input("Enter to continue")


def docker_service_commands():
    os.system("clear")
    logo.main_menu()
    cmd = input('''\n\nEnter the service commands:
        1. to start the docker service
        2. to stop the docker service
        3. to check the status of docker service
        Enter your choice here: ''')
    service = "status"
    if int(cmd) == 1:
        service = "start"
    elif int(cmd) == 2:
        service = "stop"
    print(os.system('systemctl {} docker'.format(service)))
    input("Enter to continue")


def view_instance():
    os.system("clear")
    logo.main_menu()
    os.system("docker ps")
    input("Enter to continue")


def view_all_instance():
    os.system("clear")
    logo.main_menu()
    os.system("docker ps -a")
    input("Enter to continue")

def create_container():
    os.system("clear")
    logo.main_menu()
    print("""which OS container you want to create""")
    os.system('docker images')
    img_name = input('select the OS from the available docker images: ')
    tag = input('Give the version OS which you want to launch from the available images: ')
    os_name = input('give a name to the container os: ')
    os.system('docker run -it --name {} {}:{}'.format(os_name,img_name,tag))

def attach_container():
    os.system("clear")
    logo.main_menu()
    print('\n\ncurrent running containers as: ')
    os.system("docker ps")
    attach_os = input('name or ID of the container you want to attach')
    os.system('docker attach {}'.format(attach_os))

