from __future__ import print_function
import json
import boto3
import time
import urllib
print('Loading function')

s3 = boto3.client('s3')

def lambda_handler(event, context):
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.unquote_plus(event['Records'][0]['s3']['object']['key'])
    target_bucket = 'enigma-target'
    copy_source = {'Bucket':source_bucket, 'Key':key}
    
    # Just print function  
    print("Log stream name:", context.log_stream_name)
    print("Log group name:",  context.log_group_name)
    print("Request ID:",context.aws_request_id)
    print("Mem. limits(MB):", context.memory_limit_in_mb)
    
    
    try:
        print("Using waiter to waiting for object to persist thru s3 service")
        waiter = s3.get_waiter('object_exists')
        waiter.wait(Bucket=source_bucket, Key=key)
        
        print ("Copying object from Source S3 bucket to Traget S3 bucket ")
        s3.copy_object(Bucket=target_bucket, Key=key, CopySource=copy_source)
        
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist '
              'and your bucket is in the same region as this '
              'function.'.format(key, source_bucket))
        raise e
