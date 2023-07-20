#pip install pytube
from pytube import YouTube
from sys import argv

link = argv[1]  #this is from sys
yt = YouTube(link)

print("Title: ", yt.title)  #to check the title

print("View: ", yt.views)   #to check the views

dl = yt.streams.get_highest_resolution() #to download the highest resolution possible

dl.download("C:\\Users\\aguir\\Videos\\youtube downloader") #the path where the vid go to

#TERMINAL CODE EXAMPLE:
# cd "C:\Users\aguir\PycharmProjects\pythonProject3\python projects\automate python"
#python ytDownloader.py "https://www.youtube.com/watch?v=VINRHY7dm4s&ab_channel=Titaniadota"

