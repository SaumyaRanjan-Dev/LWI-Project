import boto3
import pymongo

# AWS Configuration
def configure_aws_session():
    session = boto3.Session(
        aws_access_key_id='YOUR_ACCESS_KEY',         # Replace with your Access Key
        aws_secret_access_key='YOUR_SECRET_KEY',     # Replace with your Secret Key
        region_name='YOUR_REGION'                    # Replace with your AWS region
    )
    return session

# Function to launch an EC2 instance
def launch_ec2_instance(session):
    ec2_client = session.client('ec2')
    response = ec2_client.run_instances(
        ImageId='ami-0abcdef1234567890',  # Replace with a valid AMI ID for your region
        InstanceType='t2.micro',
        KeyName='your-key-pair-name',  # Replace with your key pair name
        MinCount=1,
        MaxCount=1
    )
    instance_id = response['Instances'][0]['InstanceId']
    print(f"EC2 instance launched with ID: {instance_id}")

# Function to launch a RHEL GUI instance in the cloud
def launch_rhel_gui_instance(session):
    ec2_client = session.client('ec2')
    response = ec2_client.run_instances(
        ImageId='ami-0abcdef1234567890',  # Replace with a valid RHEL AMI ID for your region
        InstanceType='t2.large',  # Use a suitable instance type for GUI
        KeyName='your-key-pair-name',  # Replace with your key pair name
        MinCount=1,
        MaxCount=1
    )
    instance_id = response['Instances'][0]['InstanceId']
    print(f"RHEL GUI instance launched with ID: {instance_id}")

# Function to access logs from the cloud
def access_logs_from_cloud(session):
    logs_client = session.client('logs')
    log_group_name = input("Enter the log group name: ")
    log_stream_name = input("Enter the log stream name: ")
    
    response = logs_client.get_log_events(
        logGroupName=log_group_name,
        logStreamName=log_stream_name,
        startFromHead=True
    )
    
    print("Log events:")
    for event in response['events']:
        print(event['message'])

# Function to create an event-driven architecture for audio transcription
def create_event_driven_architecture(session):
    transcribe_client = session.client('transcribe')
    bucket_name = input("Enter S3 bucket name: ")
    file_name = input("Enter the audio file name: ")

    job_name = f"TranscriptionJob-{file_name.split('.')[0]}"
    file_uri = f"s3://{bucket_name}/{file_name}"
    
    response = transcribe_client.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={'MediaFileUri': file_uri},
        MediaFormat='mp3',  # Replace with the appropriate format (e.g., wav, mp4)
        LanguageCode='en-US'
    )
    
    print(f"Transcription job started: {job_name}")
    # Add code to poll the job status and retrieve the transcript if needed

# Function to connect Python to MongoDB service via AWS Lambda
def connect_python_to_mongodb():
    mongo_uri = "your_mongo_db_uri"  # Replace with your MongoDB URI
    client = pymongo.MongoClient(mongo_uri)
    
    db = client.test  # Replace 'test' with your database name
    collection = db.your_collection  # Replace 'your_collection' with your collection name
    
    # Example: Insert a document
    document = {"name": "Gourav", "occupation": "Engineer"}
    collection.insert_one(document)
    print(f"Inserted document into MongoDB: {document}")

# Function to upload an object to S3
def upload_object_to_s3(session):
    s3_client = session.client('s3')
    bucket_name = input("Enter S3 bucket name: ")
    file_path = input("Enter the file path to upload: ")
    s3_key = file_path.split("/")[-1]

    try:
        s3_client.upload_file(file_path, bucket_name, s3_key)
        print(f"File '{file_path}' uploaded to bucket '{bucket_name}' with key '{s3_key}'")
    except Exception as e:
        print(f"Error uploading file: {e}")

# Function to integrate Lambda with S3 and SES
def integrate_lambda_with_s3_and_ses(session):
    s3_client = session.client('s3')
    ses_client = session.client('ses')
    
    bucket_name = input("Enter the S3 bucket name: ")
    file_name = input("Enter the file name with email IDs: ")
    
    # Download file from S3
    s3_client.download_file(bucket_name, file_name, '/tmp/' + file_name)
    
    # Read email IDs from file
    with open('/tmp/' + file_name, 'r') as file:
        email_ids = file.read().splitlines()
    
    # Send emails using SES
    for email in email_ids:
        response = ses_client.send_email(
            Source='your_email@example.com',  # Replace with your verified SES email
            Destination={
                'ToAddresses': [email]
            },
            Message={
                'Subject': {
                    'Data': 'Hello from AWS SES'
                },
                'Body': {
                    'Text': {
                        'Data': 'This is a test email sent from AWS SES using Boto3.'
                    }
                }
            }
        )
        print(f"Email sent to {email}")

# Menu to call all functions
def menu():
    session = configure_aws_session()
    
    while True:
        print("\nAWS Cloud Menu:")
        print("1. Launch EC2 Instance")
        print("2. Launch RHEL GUI Instance in Cloud")
        print("3. Access Logs from Cloud")
        print("4. Create Event-Driven Architecture for Audio Transcription")
        print("5. Connect Python to MongoDB Service via Lambda")
        print("6. Upload Object to S3")
        print("7. Integrate Lambda with S3 and SES")
        print("8. Exit")
        
        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            launch_ec2_instance(session)
        elif choice == '2':
            launch_rhel_gui_instance(session)
        elif choice == '3':
            access_logs_from_cloud(session)
        elif choice == '4':
            create_event_driven_architecture(session)
        elif choice == '5':
            connect_python_to_mongodb()
        elif choice == '6':
            upload_object_to_s3(session)
        elif choice == '7':
            integrate_lambda_with_s3_and_ses(session)
        elif choice == '8':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    menu()
