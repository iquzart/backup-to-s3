#!/usr/bin/python
import os
import time
import tarfile
import boto3
import progressbar
from slack_client import slack_message 

try: 
    s3 = boto3.client('s3',
         aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
        aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"],
        region_name=os.environ["AWS_DEFAULT_REGION"]
        )

    bucket_name = 'alpine-backup-01'

    archive_location = '/tmp/'
    file_name = 'backup-'+time.strftime("%Y%m%d-%H%M%S")+'.tar.gz'
    archive_source = '/tmp/test'

    with tarfile.open(archive_location+file_name, mode='w:gz') as archive:
        archive.add(archive_source, recursive=True)



    statinfo = os.stat(archive_location+file_name)
    up_progress = progressbar.progressbar.ProgressBar(maxval=statinfo.st_size)
    up_progress.start()
    def upload_progress(chunk):
        up_progress.update(up_progress.currval + chunk)

 
        s3.upload_file(
        Bucket = bucket_name,
        Filename=archive_location+file_name,
        Key=file_name,
        Callback=upload_progress,
        ExtraArgs= {"Metadata": 
            {"AppName":"Wordpress",
            "Retention":"30Days",
            }}
         )   
    up_progress.finish()
except BaseException as e:
    slack_message(e)
