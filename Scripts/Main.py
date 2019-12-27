#-----------CLASS IMPORTS------------------
import _getWeatherData as GetWeatherDataFile
import _createImage as CreateImageFile
import _S3BucketUpload as S3BucketUploadFile
import _instagramUpload as InstagramUploadFile

def main():
    try:
        weather = list(GetWeatherDataFile.GetWeather().wunderground())
    except:
        weather = list(GetWeatherDataFile.GetWeather().weatherCom())
    
    image = CreateImageFile.CreateImage(weather)
    
    fileName = image.newImage()
    
    postImage = InstagramUploadFile.InstagramUpload(fileName)
    
    postImage.postImage()
    
if __name__ == "__main__":
    main()
