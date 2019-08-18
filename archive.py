import os
import time
import tarfile
import logging
from S3_upload import upload


def archive():
    archive_location = '/tmp/'
    file_name = 'backup-'+time.strftime("%Y%m%d-%H%M%S")+'.tar.gz'
    archive_source = os.environ["ARCHIVE_SOURCE"]
    bucket_name = os.environ["BUCKET_NAME"]

    logging.basicConfig(format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        level=logging.INFO)

    try:
        logging.info('archive process started - sit tight!')
        with tarfile.open(archive_location+file_name, mode='w:gz') as archive:
             archive.add(archive_source, recursive=True)

    except OSError as error:
        logging.error('archive failed')
        logging.error('%s',error)
    else:
         size = round(os.path.getsize(archive_location+file_name)/(1024*1024.0))
         logging.info('archive has been completed - %s%s - size: %sM',archive_location,file_name,size)


         logging.info('uploading backup to s3 bucket - %s',bucket_name)
#         upload(archive_location, file_name)


         logging.info('clearing the local backup file - %s%s',archive_location,file_name)
#         os.remove(archive_location+file_name)

archive ()
