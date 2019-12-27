#-----------CLASS IMPORTS------------------
import _getWeatherData as GetWeatherDataFile
import _createImage as CreateImageFile
import _S3BucketUpload as S3BucketUploadFile
import _instagramUpload as InstagramUploadFile

#-----------JOB SCHEDULER------------------
from apscheduler.schedulers.blocking import BlockingScheduler

def job_1():
    try:
        weather = list(GetWeatherDataFile.GetWeather().wunderground())
    except:
        weather = list(GetWeatherDataFile.GetWeather().weatherCom())
    
    image = CreateImageFile.CreateImage(weather)
    
    fileName = image.newImage()
    
    postImage = InstagramUploadFile.InstagramUpload(fileName)
    
    postImage.postImage()
    

def main():
    scheduler = BlockingScheduler()
    scheduler.add_job(job_1, 'interval', hours=1)
    scheduler.start()
if __name__ == "__main__":
    main()
