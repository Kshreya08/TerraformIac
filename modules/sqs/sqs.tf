resource "aws_sqs_queue" "this" {
  name = var.queue_name  # Use the queue_name variable
}

output "queue_url" {
  value = aws_sqs_queue.this.url  # Output the URL of the queue
}
