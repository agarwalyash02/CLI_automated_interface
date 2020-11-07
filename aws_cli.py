import os

def load_cmds_aws():
    while True:
        os.system("cls")
        print("""
        Press 1 to setup EC2 instance
        Press 2 to check current EC2 instances
        Press 3 to set up CloudFront distribution
        Press 4 to create an S3 bucket
        press 9 return to main menu
        """)
        aws_a=input()
        if int(aws_a)==1:
            create_ec2()
        elif int(aws_a)==2:
            check_running_instances()
        elif int(aws_a)==3:
            pass
        elif int(aws_a)==4:
            create_S3_bucket()
        elif int(aws_a)==9:
            break
        else:
            print("Incorrect input please try again")
            input("Enter to continue")


def create_ec2():
    print("\n")
    ami_type=["ami-0e306788ff2473ccb","ami-052c08d70def0ac62","ami-0b2f6494ff0b07a0e","ami-0cda377a1b884a1bc"]
    machine_size=['t2.nano','t2.micro','t2.small','t2.medium']
    preference=dict()

    print("""select the AMI you want to use
    1. Amazon Linux 2
    2. RHEL 8
    3. Windows Server (GUI)
    4. Ubuntu 20.04
            """)
    machine_type=input()
    preference['machine_type']=ami_type[int(machine_type)-1]

    print("""Select machine type
        1. t2.nano
        2. t2.micro(free tier eligible)
        3. t2.small
        4. t2.medium """
    )
    size=input()
    preference['size']=machine_size[int(size)-1]

    num_of_inputs=int(input("How many instances you want to create \n"))
    preference['number_of_instances']=num_of_inputs
    print(f"aws ec2 run-instances --image-id {preference['machine_type']} --count {preference['number_of_instances']} --instance-type {preference['size']}")
    os.system(f"aws ec2 run-instances --image-id {preference['machine_type']} --count {preference['number_of_instances']} --instance-type {preference['size']}")
    input("Enter to continue")

def check_running_instances():
    os.system("aws ec2 describe-instances")
    input("Enter to continue")

def create_cloudfront_distribution():
    print("""
        Creates a new web distribution. You create a CloudFront distribution
        to tell CloudFront where you want content to be delivered from, and
        the details about how to track and manage content delivery. Send a
        "POST" request to the "/*CloudFront API version* /distribution"
        /"distribution ID" resource.\n\n\n"""
        )
    origin_name=input("What is the origin name\n")
    os.system(f"aws cloudfront create-distribution --origin-domain-name {origin_name}")
    input("Enter to continue")

def create_S3_bucket():
    region_actual=['ap-south-1','us-east-1','us-east-1']
    bucket_name=input("Enter the name of the bucket ")
    r_count=input("""
        Select the region where you want to create the bucket.
        1. Mumbai
        2. North Virginia
        3. U.S East
    """)
    if int(r_count) not in range(1,4):
        print("Invalid Attempt")
    else:
        os.system(f"aws s3api create-bucket --bucket {bucket_name} --region {region_actual[int(r_count)]}")
    input("Enter to continue")
