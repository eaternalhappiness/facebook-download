
import re
import requests
import urllib.request


link=input("Enter Url Here:")
#Get Url Data
html=requests.get(link)

#parse Url
try:
    url=re.search('hd_src:"(.+?)"',html.text)[1]
    print("HD Video")
    
except:
    url=re.search('sd_src:"(.+?)"',html.text)[1]
    print("SD Video")


#Download File
print("Downloading....")
urllib.request.urlretrieve(url, 'Video.mp4')
print("Download Successfull")
