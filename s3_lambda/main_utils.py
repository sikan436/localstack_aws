import os
import logging
import json
from zipfile import ZipFile
import boto3


AWS_REGION = 'us-east-1'
AWS_PROFILE = 'localstack'
LOCALSTACK_ENDPOINT_URL='http://localhost:4566'
ENDPOINT_URL='http://localhost:4566'

LAMBDA_ZIP = './function.zip'
boto3.setup_default_session(profile_name=AWS_PROFILE)
# logger config
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')


def get_boto3_resource(service):
    """
    Initialize Boto3 Lambda client.
    """
    try:
        resource=    boto3.resource(
            service,
            region_name=AWS_REGION,
            endpoint_url=LOCALSTACK_ENDPOINT_URL
        )
    except Exception as e:
        logger.exception('Error while connecting to LocalStack.')
        raise e
    else:
        return resource

def get_boto3_client(service):
    """
    Initialize Boto3 Lambda client.
    """
    try:
        lambda_client = boto3.client(
            service,
            region_name=AWS_REGION,
            endpoint_url=ENDPOINT_URL
        )
    except Exception as e:
        logger.exception('Error while connecting to LocalStack.')
        raise e
    else:
        return lambda_client

def create_lambda_zip(function_name):
    """
    Generate ZIP file for lambda function.
    """
    try:
        with ZipFile(LAMBDA_ZIP, 'w') as zip:
            zip.write(function_name + '.py')
    except Exception as e:
        logger.exception('Error while creating ZIP file.')
        raise e



def create_lambda(function_name,**kw_args):
    """
    Creates a Lambda function in LocalStack.
    """
    try:
        lambda_client = get_boto3_client('lambda')
        _ = create_lambda_zip(function_name)
        # create zip file for lambda function.
        with open(LAMBDA_ZIP, 'rb') as f:
            zipped_code = f.read()
        lambda_client.create_function(
            FunctionName=function_name,
            Runtime='python3.8',
            Role='arn:aws:iam::000000000000:role/lambda-role',
            Handler=function_name + '.handler',
            Code=dict(ZipFile=zipped_code),
            **kw_args
            
        )
    except Exception as e:
        logger.exception('Error while creating function.')
        raise e

def delete_lambda(function_name):
    """
    Deletes the specified lambda function.
    """
    try:
        lambda_client = get_boto3_client('lambda')
        lambda_client.delete_function(
            FunctionName=function_name
        )
        # remove the lambda function zip file
        os.remove(LAMBDA_ZIP)
    except Exception as e:
        logger.exception('Error while deleting lambda function')
        raise e

def invoke_function(function_name):
    """
    Invokes the specified function and returns the result.
    """
    try:
        lambda_client = get_boto3_client('lambda')
        response = lambda_client.invoke(
            FunctionName=function_name)
        return json.loads(
            response['Payload']
            .read()
            .decode('utf-8')
        )
    except Exception as e:
        logger.exception('Error while invoking function')
        raise e
    
def create_bucket(bucket_name):
    try:
        s3_client=get_boto3_client('s3')
        s3_client.create_bucket(Bucket=bucket_name)
    except Exception as e:
        logger.exception('error while creating s3 bucket'
                         )
        raise e

def s3_upload_file(bucket_name,object_name,content):
    try:
        s3_client=get_boto3_client('s3')
        s3_client.put_object(Bucket=bucket_name,key=object_name,Body=content)
    except Exception as e:
        logger.exception('unable to load file to s3')
        return e
    
def list_s3_bucket_objects(bucket_name):
    try:
        s3_resource=get_boto3_resource('s3')
        logger.info(f'list of s3 files in {bucket_name} below')
        return {
             obj.key for obj in s3_resource.Bucket(bucket_name).objects.all()

        }
    except Exception as e:
        logger.exception(f'unable to list files in s3 bucket {bucket_name}')
    
