# variables.tf
variable "instance_type" {
  description = "EC2 instance type"
  default     = "t2.micro"
}

variable "s3_bucket_name" {
  description = "Name of the S3 bucket"
  default     = "my-localstack-s3-bucket"
}

variable "queue_name" {
  description = "Name of the SQS queue"
  default     = "my-localstack-queue"
}

variable "secret_name" {
  description = "Name of the Secrets Manager secret"
  default     = "my-localstack-secret"
}
