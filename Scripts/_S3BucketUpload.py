#----------S3 BUCKET IMPORTS------------

import boto3

class S3Upload:
    def __init__(self, fileToBeUploaded):
        
        self.fileToBeUploaded = fileToBeUploaded
        
        print(self.fileToBeUploaded)
        
    def uploadFile(self):
        try:
            Key = self.fileToBeUploaded
            
            bucketName = 'instaweather'
            
            outputName = 'worked.png'
            
            s3 = boto3.client('s3')
            
            s3.upload_file(Key, bucketName, outputName)

            print('----------FILE UPLOADED-----------')
            
        except Exception as e: 
            print('File failed to upload. Error: '+ str(e))
