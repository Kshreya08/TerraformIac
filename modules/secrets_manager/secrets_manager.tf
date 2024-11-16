
resource "aws_secretsmanager_secret" "this" {
  name = var.secret_name
}

resource "aws_secretsmanager_secret_version" "this" {
  secret_id     = aws_secretsmanager_secret.this.id
  secret_string = jsonencode({
    username = "admin"
    password = "mysecretpassword123"
    host     = "localhost"
    port     = 5432
    database = "myapp"
  })
}

output "secret_arn" {
  value = aws_secretsmanager_secret.this.arn
}
