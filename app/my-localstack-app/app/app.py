import os
import boto3
import json
from datetime import datetime
from dotenv import load_dotenv
from pathlib import Path
import time

# Load environment variables
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class LocalStackServices:
    def __init__(self):
        # Get configuration from environment variables
        self.endpoint_url = os.getenv('LOCALSTACK_ENDPOINT')
        self.region = os.getenv('AWS_DEFAULT_REGION')
        self.access_key = os.getenv('AWS_ACCESS_KEY_ID')
        self.secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
        
        # Resource names
        self.bucket_name = os.getenv('BUCKET_NAME')
        self.queue_name = os.getenv('QUEUE_NAME')
        self.secret_name = os.getenv('SECRET_NAME')
        
        # Initialize clients
        self.init_clients()

    def init_clients(self):
        """Initialize AWS service clients"""
        client_config = {
            'endpoint_url': self.endpoint_url,
            'region_name': self.region,
            'aws_access_key_id': self.access_key,
            'aws_secret_access_key': self.secret_key
        }

        self.s3 = boto3.client('s3', **client_config)
        self.sqs = boto3.client('sqs', **client_config)
        self.secrets = boto3.client('secretsmanager', **client_config)
        
        # Get queue URL
        try:
            response = self.sqs.get_queue_url(QueueName=self.queue_name)
            self.queue_url = response['QueueUrl']
        except:
            self.queue_url = f"{self.endpoint_url}/000000000000/{self.queue_name}"

    def verify_resources(self):
        """Verify and create resources if they don't exist"""
        print("\n=== Verifying Resources ===")
        
        # Verify SQS Queue
        try:
            self.sqs.get_queue_url(QueueName=self.queue_name)
            print(" SQS Queue exists")
        except:
            try:
                self.sqs.create_queue(QueueName=self.queue_name)
                print(" SQS Queue created")
            except Exception as e:
                print(f" Failed to create SQS Queue: {str(e)}")

        # Verify Secret
        try:
            self.secrets.describe_secret(SecretId=self.secret_name)
            print(" Secret exists")
        except:
            try:
                secret_value = {
                    "username": "admin",
                    "password": "mysecretpassword123",
                    "host": "localhost",
                    "port": 5432,
                    "database": "myapp"
                }
                self.secrets.create_secret(
                    Name=self.secret_name,
                    SecretString=json.dumps(secret_value)
                )
                print(" Secret created")
            except Exception as e:
                print(f" Failed to create Secret: {str(e)}")

        # Verify S3 Bucket
        try:
            self.s3.head_bucket(Bucket=self.bucket_name)
            print(" S3 Bucket exists")
        except:
            try:
                self.s3.create_bucket(Bucket=self.bucket_name)
                print(" S3 Bucket created")
            except Exception as e:
                print(f" Failed to create S3 Bucket: {str(e)}")

    def test_s3(self):
        """Test S3 operations"""
        print("\n=== Testing S3 Operations ===")
        
        # Upload test
        try:
            content = f"Test content generated at {datetime.now()}"
            self.s3.put_object(
                Bucket=self.bucket_name,
                Key="test.txt",
                Body=content
            )
            print(" Upload successful")
        except Exception as e:
            print(f" Upload failed: {str(e)}")
            return

        # Download test
        try:
            response = self.s3.get_object(
                Bucket=self.bucket_name,
                Key="test.txt"
            )
            content = response['Body'].read().decode('utf-8')
            print(f" Downloaded content: {content}")
        except Exception as e:
            print(f" Download failed: {str(e)}")

    def test_sqs(self):
        """Test SQS operations"""
        print("\n=== Testing SQS Operations ===")
        
        # Send message
        try:
            message = {
                'text': 'Test message',
                'timestamp': str(datetime.now())
            }
            response = self.sqs.send_message(
                QueueUrl=self.queue_url,
                MessageBody=json.dumps(message)
            )
            print(f" Message sent. ID: {response['MessageId']}")
        except Exception as e:
            print(f" Send failed: {str(e)}")
            return

        # Receive message
        try:
            response = self.sqs.receive_message(
                QueueUrl=self.queue_url,
                MaxNumberOfMessages=1,
                WaitTimeSeconds=5
            )
            
            if 'Messages' in response:
                for msg in response['Messages']:
                    print(f" Received message: {msg['Body']}")
                    # Delete the message
                    self.sqs.delete_message(
                        QueueUrl=self.queue_url,
                        ReceiptHandle=msg['ReceiptHandle']
                    )
            else:
                print("ℹ️ No messages available")
        except Exception as e:
            print(f" Receive failed: {str(e)}")

    def test_secrets(self):
        """Test Secrets Manager operations"""
        print("\n=== Testing Secrets Manager Operations ===")
        
        try:
            response = self.secrets.get_secret_value(
                SecretId=self.secret_name
            )
            secret_data = json.loads(response['SecretString'])
            print(f"Retrieved secret: {json.dumps(secret_data, indent=2)}")
        except Exception as e:
            print(f" Secret retrieval failed: {str(e)}")

def main():
    services = LocalStackServices()
    
    # Verify resources exist
    services.verify_resources()
    
    # Wait a moment for resources to be fully created
    time.sleep(2)
    
    # Test all services
    services.test_s3()
    services.test_sqs()
    services.test_secrets()

if __name__ == "__main__":
    main()
