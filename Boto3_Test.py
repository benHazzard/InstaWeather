import boto3

s3 = boto3.client('s3')

#Upload example image
bucketName = 'instaweather'
Key = 'examplefile.jpg'
outPutName = 'outputedfile.jpg'

s3 = boto3.client('s3')
s3.upload_file(Key,bucketName,outPutName)
