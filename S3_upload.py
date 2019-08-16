import os
import boto3
import progressbar




def upload(archive_location,file_name):

    s3 = boto3.client('s3',
        aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
        aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"],
        region_name=os.environ["AWS_DEFAULT_REGION"]
        )

    bucket_name = 'alpine-backup-01'
   
    #print ("Uploading Archive to s3 bucket") 
    s3.upload_file(
           Bucket = bucket_name,
           Filename=archive_location+file_name,
           Key=file_name,
#           Callback=upload_progress,
           ExtraArgs= {"Metadata": 
               {"AppName":"Wordpress",
                "Retention":"30Days",
               }}
            ) 
