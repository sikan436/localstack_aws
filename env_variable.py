import os 
import boto3

aws_access_key_id = 'test'
aws_secret_access_key = 'test'
AWS_PROFILE='localstack'
region = 'us-east-1'
endpoint_url='http://localhost:4566'

boto3.setup_default_session(prfile_name=AWS_PROFILE)

localstack_client=boto3.client('s3',region_name=region,endpoint_url=endpoint_url)


