#!/usr/bin/env python3

import logging
import boto3
from botocore.exceptions import ClientError
import json 
import os
AWS_REGION= 'us-east-1'
AWS_PROFILE='localstack'
ENDPOINT_URL='http://localhost:4566'
#logger config
logger=logging.getLogger()
logging.basicConfig(level=logging.INFO)
boto3.setup_default_session(profile_name=AWS_PROFILE)
s3_client = boto3.client("s3", region_name=AWS_REGION,endpoint_url=ENDPOINT_URL)
s3_resource=boto3.resource("s3", region_name=AWS_REGION,endpoint_url=ENDPOINT_URL)
def create_bucket(bucket_name):
 
    try:
        response = s3_client.create_bucket(Bucket=bucket_name)
    except ClientError:
        logger.exception('counldnt create s3 locally')
        raise
    else:
        return response

def list_bucket():
    try:
        response=s3_resource.buckets.all()
    except ClientError:
         logger.exception('counldnt list the directory locally')
    else:
        return response

def upload_file(file_name,bucket,object_name=None):
    try:
        if object_name is None:
            object_name=os.path.basename(file_name)
        response=s3_client.upload_file(file_name,bucket,object_name)
    except ClientError:
        logger.exception('unable to load file in s3')
    else:
        return response
    
def list_files(bucket_name):
    try:
     s3_bucket=s3_resource.Bucket(bucket_name)

    except ClientError:
        logger.exception(f'unable list files  in bucket {bucket_name}')
    else:
        return s3_bucket
        

def main():

    bucket_name= "hands-on-cloud-localstack-bucket2"
    logger.info('creating local bucket') 
    s3= create_bucket(bucket_name)
    logger.info('53 bucket created.')
    logger.info(json.dumps (s3, indent=4) + '\n')
    
    logger.info('now starting upload file')
    filename='C:\\Users\\asus\\Downloads\\image.png'
    object_name=None
    # object_name='image.png'
    s3=upload_file(filename,bucket_name,object_name)
    logger.info('file successsfully uploaded')
    s3=list_bucket()
    logger.info('listing buckets')
    for bucket in s3:
        logger.info(bucket.name)
        logger.info('listing files')
        s2=list_files(bucket.name)
        for obj in s2.objects.all():
                logger.info(f'-- {obj.key}')
                if obj.key is None:
                    logger.info('empty bucket')




if __name__=='__main__':
    main()