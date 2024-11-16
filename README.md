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

## Prerequisites

- LocalStack (latest version)
- Terraform >= 1.0.0
- Python >= 3.8
- Docker
- AWS CLI

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
Region: us-east-1
```

4. **Deploy Infrastructure with Terraform**
```bash
cd terraform
terraform init
terraform plan
terraform apply
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
- Visibility timeout: 30 seconds

### Amazon S3
- Bucket for file storage
- Versioning enabled
- Server-side encryption

### AWS Secrets Manager
- Stores application secrets
- Automatic rotation enabled
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
export AWS_DEFAULT_REGION=us-east-1
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

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

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



## Acknowledgments

- [LocalStack Documentation](https://docs.localstack.cloud)
- [Terraform Documentation](https://www.terraform.io/docs)
- [AWS SDK for Python (Boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
