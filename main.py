from pytube import YouTube

link = input("link:")
url = YouTube(link)
download_path = r"C:\\Users\h-a-m\\Desktop\\test_download"

   # process
try:
        url = YouTube(link)
        video = url.streams.get_lowest_resolution()
        print("Downloading....")
        video.download(download_path)
        print("Download Succesfull")
except:
        print("Error")
