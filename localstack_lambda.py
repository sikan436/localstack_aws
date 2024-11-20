# #!/usr/bin/env python3
# from zipfile import ZipFile 
# import logging
# import boto3
# from botocore.exceptions import ClientError
# import json 
# import os
# AWS_REGION= 'us-east-1'
# AWS_PROFILE='localstack'
# ENDPOINT_URL='http://localhost:4566'
# lambda_zip='./function.zip'
# #logger config
# logger=logging.getLogger()
# logging.basicConfig(level=logging.INFO)
# boto3.setup_default_session(profile_name=AWS_PROFILE)
# # s3_client = boto3.client("s3", region_name=AWS_REGION,endpoint_url=ENDPOINT_URL)
# # s3_resource=boto3.resource("s3", region_name=AWS_REGION,endpoint_url=ENDPOINT_URL)


# def get_boto3_client(service):
#     try:
#         lambda_client=boto3.client(service,region_name=AWS_REGION,endpoint_url=ENDPOINT_URL)
#     except Exception as e:
#         logger.exception('error while lambda client localstack')
#         raise e
#     else :
#         return lambda_client
    

# def create_lambda_zip(function_name):
#     try:
#         with ZipFile(lambda_zip,'w') as zip:
#             zip.write(function_name+'.py')
#     except Exception as e:
#         logger.exception('error while zip file ')
#         raise e


# def create_lambda(function_name):
#     """
#     Creates a Lambda function in LocalStack.
#     """
#     try:
#         lambda_client = get_boto3_client('lambda')
#         _ = create_lambda_zip(function_name)
#         # create zip file for lambda function.
#         with open(lambda_zip, 'rb') as f:
#             zipped_code = f.read()
#         lambda_client.create_function(
#             FunctionName=function_name,
#             Runtime='python3.8',
#             Role='role',
#             Handler=function_name + '.handler',
#             Code=dict(ZipFile=zipped_code)
#         )
#     except Exception as e:
#         logger.exception('Error while creating function.')
#         raise e 

# # def create_lambda(function_name):
# #     try:
# #         lambda_client=get_boto3_client('lambda')
# #         _ = create_lambda_zip(function_name)

# #         with open(lambda_zip,'rb') as f:
# #             zipped_code=f.read()

# #         lambda_client.create_function(FunctionName=function_name,Runtime='python3.12.2',Role='role_arn',Handler=function_name +'.handler',Code=dict(ZipFile=zipped_code))

# #     except Exception as  e:
# #         logger.exception('error in create lambda function')
# #         raise e        
    
# def delete_lambda(function_name):
#     try:
#         lambda_client=get_boto3_client('lambda')
#         lambda_client.delete_function(FunctionName=function_name)
#         os.remove(lambda_zip)

#     except Exception as e :
#         logger.exception('error while deleting lambda function')
#         raise e 
    
# def invoke_function(function_name):
#     try:
#         lambda_client=get_boto3_client('lambda')
#         response=lambda_client.invoke(FunctionName=function_name)
#         return json.loads(response['Payload'].read().decode('utf-8'))
#     except  Exception as e:
#         logger.exception('error while invoking function')
#         raise e
        


    


