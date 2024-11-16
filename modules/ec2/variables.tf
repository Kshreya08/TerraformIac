variable "instance_type" {
  description = "The type of EC2 instance"
  type        = string
  default     = "t2.micro"  # Default value, can be overridden when calling the module
}

variable "ami" {
  description = "The AMI ID to use for the instance"
  type        = string
  default     = "ami-0c55b159cbfafe1f0"  # Update with your desired AMI ID or use a default for simplicity
}
