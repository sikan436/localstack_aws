
import logging 
import os 
import boto3
#Logger config
logger= logging.getLogger()
logging.basicConfig(level=logging.INFO,
format='(asctime)s: (levelname)s: (message)s')
AWS_REGION = os.environ.get('AWS REGION", "us-east-1') 
LOCALSTACK= os.environ.get('LOCALSTACK', None)
LOCALSTACK_ENDPOINT_URL= os.environ.get('LOCALSTACK_ENDPOINT_URL', 'http://host.docker.internal:4566')

def configure_aws_env():
    if LOCALSTACK:
        os.environ['AWS_ACCESS_KEY_ID'] = 'test'
        os.environ['AWS_SECRET_ACCESS_KEY'] = 'test' 
        os.environ['AWS DEFAULT REGION']= AWS_REGION
    boto3.setup_default_session()
def get_boto3_client(service):

    try:
        configure_aws_env()
        boto3_client = boto3.client(
service,
region_name=AWS_REGION,
endpoint_url=LOCALSTACK_ENDPOINT_URL)
    except Exception as e:

        logger.exception('unable to connect to localstack')
        raise e
    else:
        return boto3_client
def handler(event, context):
    s3_client = get_boto3_client('s3')
    logging.info('uploading object to s3 cloud') 
    bucket_name='hands-on-cloud-bucket'
    object_key ='hands-on-cloud.txt'
    s3_client.put_object(Bucket='hands-on-cloud-bucket',Key=object_key,
        Body='localstack-boto3-python')
    return {
                "message": "Object uploaded to 53"}
    