from bs4 import BeautifulSoup
import requests
import os
import errno
import random
import shutil


subreddit = input("Enter the subreddit you wish to download images from: ")
subreddit = "wallpapers"
r = requests.get("http://www.reddit.com/r/" + subreddit)


data =r.text
soup = BeautifulSoup(data)
#print(soup.prettify())

#f = open("Untitled Document", 'r')
#soup = BeautifulSoup(f)

#f.close()


try:
    os.chdir(os.getcwd() + "/wallpapers")

except OSError as e:
    os.makedirs("/wallpapers")
    os.chdir(os.getcwd() +"/wallpapers")



links = soup.find_all('a')
i = 1
for link in links:
    url = link.get('href')

    url = str(url)
    if str(url[0:10]) == "http://i.i":
        data = requests.get(url, stream = True)
        try:
            with open(str(i), "wb") as outFile:
                print("downloading")
                for chunk in data.iter_content(128):
                    outFile.write(chunk)
        except errno as e:
            print(e)

    i+=1

img = random.choice(os.listdir())
os.system("gsettings set org.gnome.desktop.background picture-uri file://" + os.getcwd() + "/" + img)
