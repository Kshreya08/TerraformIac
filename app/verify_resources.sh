#!/bin/bash

echo "Checking S3 Buckets..."
aws --endpoint-url=http://localhost:4566 s3api list-buckets

echo -e "\nChecking SQS Queues..."
aws --endpoint-url=http://localhost:4566 sqs list-queues

echo -e "\nChecking Secrets..."
aws --endpoint-url=http://localhost:4566 secretsmanager list-secrets

echo -e "\nCreating test secret value..."
aws --endpoint-url=http://localhost:4566 secretsmanager create-secret \
    --name my-db-secret \
    --secret-string '{"username":"admin","password":"mysecretpassword123","host":"localhost","port":5432,"database":"myapp"}'

echo -e "\nCreating SQS queue..."
aws --endpoint-url=http://localhost:4566 sqs create-queue \
    --queue-name my-test-queue
