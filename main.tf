terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

# AWS provider configuration for LocalStack
provider "aws" {
  region                      = "us-west-1"
  access_key                  = "test"
  secret_key                  = "test"
  skip_credentials_validation = true
  skip_metadata_api_check     = true
  skip_requesting_account_id  = true

  # Configure endpoints for all services
  endpoints {
    ec2             = "http://localhost:4566"
    s3              = "http://localhost:4566"
    sqs             = "http://localhost:4566"
    secretsmanager  = "http://localhost:4566"
  }

  # Additional settings for proper LocalStack operation
  s3_use_path_style           = true
  #s3_force_path_style         = true
}

# Module for SQS
module "sqs" {
  source     = "./modules/sqs"
  queue_name = "my-test-queue"
}

# Module for S3
module "s3" {
  source         = "./modules/s3"
  s3_bucket_name = "my-test-bucket"
}


# Module for Secrets Manager
module "secrets_manager" {
  source      = "./modules/secrets_manager"
  secret_name = "my-db-secret"
}

# Module for EC2
module "ec2" {
  source        = "./modules/ec2"
  instance_type = "t2.micro"
  ami           = "ami-0c55b159cbfafe1f0"  # This AMI ID is fine for testing with LocalStack
}


