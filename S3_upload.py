import os
import boto3
from boto3.s3.transfer import TransferConfig
import logging

def upload(archive_location,file_name):

   s3 = boto3.client('s3',
        aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
        aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"],
        region_name=os.environ["AWS_DEFAULT_REGION"]
        )
   logging.basicConfig(format='%(asctime)s - %(message)s',
                       datefmt='%Y-%m-%d %H:%M:%S',
                       level=logging.INFO)

   bucket_name = os.environ["BUCKET_NAME"]

   config = TransferConfig(multipart_threshold=1024 ** 1024, max_concurrency=10,
                            multipart_chunksize=1024 ** 25, use_threads=True)

   try: 
         
         s3.upload_file(
              Bucket = bucket_name,
            Filename=archive_location+file_name,
            Key=file_name,
            Config=config,
            ExtraArgs= {"Metadata": 
                  {"AppName":"Wordpress",
                   "Retention":"30Days",
                  }}
               ) 
      
   except OSError as error:
          logging.error('Upload to S3 failed')
          logging.error('%s',error)
   else:
         logging.info('successfully uploaded to s3 bucket - %s',bucket_name)

