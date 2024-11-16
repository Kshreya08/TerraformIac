# LocalStack Terraform Infrastructure Project

This project demonstrates setting up a local AWS infrastructure using LocalStack and Terraform, along with a sample Python application that interacts with various AWS services.

## Project Structure
```
├── app/
│   ├── app.py                 # Main application file
│   └── requirements.txt       # Python dependencies
├── terraform/
│   ├── main.tf               # Main Terraform configuration
│   ├── variables.tf          # Variable definitions
│   ├── outputs.tf            # Output definitions
│   └── providers.tf          # Provider configurations
├── .gitignore
└── README.md
```

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Development Prerequisites</title>
    <style>
        .container {
            max-width: 800px;
            margin: 0 auto;
            font-family: Arial, sans-serif;
            padding: 20px;
        }
        .prerequisite {
            margin-bottom: 30px;
            padding: 20px;
            border-radius: 8px;
            background-color: #f5f5f5;
        }
        .prerequisite h2 {
            color: #2c3e50;
            margin-top: 0;
            border-bottom: 2px solid #3498db;
            padding-bottom: 10px;
        }
        .command-block {
            background-color: #2c3e50;
            color: #ecf0f1;
            padding: 15px;
            border-radius: 5px;
            margin: 10px 0;
            font-family: monospace;
            white-space: pre-wrap;
        }
        .verification {
            margin-top: 15px;
            padding: 10px;
            background-color: #e8f6f3;
            border-left: 4px solid #2ecc71;
        }
        .verification h3 {
            margin: 0;
            color: #27ae60;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Development Environment Prerequisites</h1>

        <div class="prerequisite">
            <h2>1. LocalStack (Latest Version)</h2>
            <div class="command-block">docker run --rm -d -p 4566:4566 -p 4510-4559:4510-4559 localstack/localstack</div>
            <div class="verification">
                <h3>Verification</h3>
                <div class="command-block">curl http://localhost:4566/_localstack/health</div>
            </div>
        </div>

        <div class="prerequisite">
            <h2>2. Terraform Installation</h2>
            <div class="command-block">sudo apt-get update && sudo apt-get install -y gnupg software-properties-common

wget -O- https://apt.releases.hashicorp.com/gpg | gpg --dearmor | sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg

echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list

sudo apt update && sudo apt-get install terraform</div>
            <div class="verification">
                <h3>Verification</h3>
                <div class="command-block">terraform --version  # Should be >= 1.0.0</div>
            </div>
        </div>

        <div class="prerequisite">
            <h2>3. Python Installation (>= 3.8)</h2>
            <div class="command-block">sudo apt update
sudo apt install python3.8 python3-pip</div>
            <div class="verification">
                <h3>Verification</h3>
                <div class="command-block">python --version  # Should be >= 3.8
pip --version</div>
            </div>
        </div>

        <div class="prerequisite">
            <h2>4. Docker Installation (Linux)</h2>
            <div class="command-block">sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
sudo systemctl start docker
sudo systemctl enable docker</div>
        </div>

        <div class="prerequisite">
            <h2>5. AWS CLI Installation</h2>
            <div class="command-block">curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install</div>
            <div class="verification">
                <h3>Verification</h3>
                <div class="command-block">aws --version</div>
            </div>
        </div>
    </div>
</body>
</html>

## Quick Start

1. **Clone the Repository**
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

2. **Start LocalStack**
```bash
localstack start
```

3. **Configure AWS CLI for LocalStack**
```bash
aws configure --profile localstack
AWS Access Key ID: test
AWS Secret Access Key: test
Region: us-west-1
```

4. **Deploy Infrastructure with Terraform**
```bash
cd terraform
terraform init ( Initialize the working directory and install dependencies.)
terraform plan(Review what changes Terraform plans to make)
terraform apply (Apply the changes as per the plan)
```

5. **Set Up Python Environment**
```bash
cd ../app
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

6. **Run the Application**
```bash
python app.py
```

## Infrastructure Components

### Amazon SQS
- Standard queue for message processing
- Message retention period: 14 days

### Amazon S3
- Bucket for file storage
- Versioning enabled
- Server-side encryption

### AWS Secrets Manager
- Stores application secrets
- Encrypted storage

### EC2 Instance
- Instance type: t2.micro
- AMI: Amazon Linux 2
- Security group with required ports

## Application Features

1. **SQS Operations**
   - Send messages to queue
   - Receive messages from queue
   - Delete processed messages

2. **S3 Operations**
   - Upload files to bucket
   - Download files from bucket
   - List bucket contents

3. **Secrets Management**
   - Retrieve secrets
   - Update secrets
   - Rotate secrets

4. **EC2 Integration**
   - Deploy application
   - Health checks
   - Instance management

## Environment Variables

```bash
export AWS_PROFILE=localstack
export AWS_DEFAULT_REGION=us-west-1
export LOCALSTACK_HOSTNAME=localhost
export LOCALSTACK_ENDPOINT=http://localhost:4566
```
```

## Troubleshooting

1. **LocalStack Issues**
   - Check if LocalStack is running
   - Verify endpoint accessibility
   - Check Docker status

2. **Terraform Issues**
   - Clear `.terraform` directory
   - Reinitialize Terraform
   - Check provider versions

3. **Python Application Issues**
   - Verify virtual environment activation
   - Check dependencies installation
   - Validate AWS credentials


## Development Commands

```bash
# Start LocalStack
localstack start

# Check LocalStack status
localstack status services

# Terraform commands
terraform init
terraform plan
terraform apply
terraform destroy

# Python virtual environment
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Git commands
git init
git add .
git commit -m "Your message"
git push origin master
```

terraform destroy


## Acknowledgments

- [LocalStack Documentation](https://docs.localstack.cloud)
- [Terraform Documentation](https://www.terraform.io/docs)
- [AWS SDK for Python (Boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
