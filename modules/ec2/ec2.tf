resource "aws_instance" "this" {
  ami           = var.ami                  # Use variable for AMI ID
  instance_type = var.instance_type        # Use variable for instance type
}

output "instance_id" {
  value = aws_instance.this.id
}
