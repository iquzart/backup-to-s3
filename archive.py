import os
import time
import tarfile
from hurry.filesize import size
from S3_upload import upload



def archive():
    archive_location = '/mnt/'
    file_name = 'backup-'+time.strftime("%Y%m%d-%H%M%S")+'.tar.gz'
    #archive_source = os.environ["ARCHIVE_SOURCE"]
    archive_source = '/home/iqbal/Downloads'


    try: 
        with tarfile.open(archive_location+file_name, mode='w:gz') as archive:
             archive.add(archive_source, recursive=True)
    except OSError as error:
        print ("Archive Failed!")
        print (error)
    else: 
         
         print ("Backup file created:",archive_location+file_name)
         print ("Archive file size: "'{:,.0f}'.format(os.path.getsize(archive_location+file_name)/float(1<<20))+" MB")
#         print (os.path.getsize(archive_location+file_name)/ (1024*1024.0))

         print ("Uploading backup to s3 bucket")
         upload(archive_location, file_name)


         print ("Clearing the local backup file:",archive_location+file_name) 
         os.remove(archive_location+file_name)
    
archive ()
