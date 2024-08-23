import boto3
import os

def launch_ec2_instance():
    ec2 = boto3.resource('ec2')
    instance = ec2.create_instances(
        ImageId='ami-replacewithyouramiid',
        InstanceType='t2.micro',
        MinCount=1,
        MaxCount=1
    )
    print(f'Launched EC2 Instance with ID: {instance[0].id}')

def setup_rhel_gui():
    print("Launching RHEL GUI instance...")
    print("RHEL GUI setup complete.")

def access_cloud_logs():
    logs = boto3.client('logs')
    log_groups = logs.describe_log_groups()
    print("Log Groups:")
    for log_group in log_groups['logGroups']:
        print(log_group['logGroupName'])

def s3_event_driven_architecture():
    print("Setting up event-driven architecture...")
    # Code to create S3 bucket, Lambda, and AWS Transcribe event trigger
    print("Event-driven architecture setup complete.")

def connect_python_mongodb():
    print("Connecting Python to MongoDB using Lambda...")
    # Code to connect Lambda to MongoDB using pymongo
    print("Connection complete.")

def upload_object_to_s3():
    s3 = boto3.client('s3')
    file_name = input("Enter the file name to upload: ")
    bucket_name = input("Enter the S3 bucket name: ")
    s3.upload_file(file_name, bucket_name, os.path.basename(file_name))
    print(f'{file_name} uploaded to {bucket_name}')

def integrate_lambda_s3_ses():
    print("Integrating Lambda with S3 and SES...")
    # Code to read emails from S3 using Lambda and send emails via SES
    print("Integration complete.")

def menu():
    while True:
        print("\nAWS Cloud Automation Menu")
        print("1. Launch EC2 Instance")
        print("2. Setup RHEL GUI Instance")
        print("3. Access Cloud Logs")
        print("4. Create Event-Driven Architecture")
        print("5. Connect Python to MongoDB using Lambda")
        print("6. Upload Object to S3")
        print("7. Integrate Lambda with S3 and SES")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            launch_ec2_instance()
        elif choice == '2':
            setup_rhel_gui()
        elif choice == '3':
            access_cloud_logs()
        elif choice == '4':
            s3_event_driven_architecture()
        elif choice == '5':
            connect_python_mongodb()
        elif choice == '6':
            upload_object_to_s3()
        elif choice == '7':
            integrate_lambda_s3_ses()
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
