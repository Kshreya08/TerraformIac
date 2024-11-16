# LocalStack Terraform Infrastructure Part1

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
### Prerequisites and Installation Guide
- **LocalStack**: Start with `docker run --rm -d -p 4566:4566 -p 4510-4559:4510-4559 localstack/localstack`
-  verify with `curl http://localhost:4566/_localstack/health`.
   
- **Terraform**: Update and install with `sudo apt-get update && sudo apt-get install -y gnupg software-properties-common wget -O- https://apt.releases.hashicorp.com/gpg | gpg --dearmor | sudo tee 
   /usr/share/keyrings/hashicorp-archive-keyring.gpg echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee 
   /etc/apt/sources.list.d/hashicorp.list sudo apt update && sudo apt-get install terraform`
- Verify the installation with `terraform --version`.
  
- **Python**: Install with `sudo apt update sudo apt install python3.8 python3-pip`
- verify with `python --version` and `pip --version`.
  
- **Docker**: Install on Linux with `sudo apt-get update sudo apt-get install docker-ce docker-ce-cli containerd.io sudo systemctl start docker sudo systemctl enable docker`.
  
- **AWS CLI**: Install by running `curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" unzip awscliv2.zip sudo ./aws/install`.


## Quick Start

1. **Clone the Repository**
```bash
git clone https://github.com/Kshreya08/TerraformIac.git
```

2. **Start LocalStack**
```bash
cd TerraformIac
```

3. **Before executing Terraform commands, make sure that the Docker container for LocalStack is up and running.**

4. **Deploy Infrastructure with Terraform**
```bash
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
python3 app.py
```
![Screenshot 2024-11-15 044241](https://github.com/user-attachments/assets/d66613eb-cd1f-45ce-a5ed-c66d8a6265d5)(Terminal)
![Screenshot 2024-11-15 060448](https://github.com/user-attachments/assets/8df33dd2-ad8b-4b14-a0bc-140ad4bc6404)(Application)

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
