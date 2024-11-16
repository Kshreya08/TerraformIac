resource "aws_s3_bucket" "this" {
  bucket = var.s3_bucket_name  # Reference the variable
}

output "bucket_name" {
  value = aws_s3_bucket.this.bucket  # Output the bucket name
}
