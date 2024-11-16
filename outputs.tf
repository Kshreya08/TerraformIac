# outputs.tf
output "s3_bucket_name" {
  value = module.s3.bucket_name
}

output "sqs_queue_url" {
  value = module.sqs.queue_url
}

output "secret_arn" {
  value = module.secrets_manager.secret_arn
}

output "ec2_instance_id" {
  value = module.ec2.instance_id
}
