import os
import time
import tarfile
from S3_upload import upload



def archive():
    archive_location = '/tmp/'
    file_name = 'backup-'+time.strftime("%Y%m%d-%H%M%S")+'.tar.gz'
    #archive_source = os.environ["Archive_Source"]''
    archive_source = '/tmp/test/'

    try: 
        with tarfile.open(archive_location+file_name, mode='w:gz') as archive:
             archive.add(archive_source, recursive=True)
    except OSError as error:
        print ("Archive Failed!")
        print (error)
    else: 
         print ("Backup file created:",archive_location+file_name)
#         print ("File size: "'{:,.0f}'.format(os.path.getsize(archive_location+file_name)/float(1<<20))+" MB")

         print ("Uploading backup to s3 bucket")
         upload(archive_location, file_name)


         print ("Clearing the local backup file:",archive_location+file_name) 
         os.remove(archive_location+file_name)
    
archive ()
