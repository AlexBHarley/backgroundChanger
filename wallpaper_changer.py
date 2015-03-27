from bs4 import BeautifulSoup
import requests
import os
    
import shutil

site_content = requests.get('http://www.reddit.com/r/wallpapers')
data = site_content.text
soup = BeautifulSoup(data)
#print(soup)
pic_list = []
for tag in soup.find_all('div', 'sitetable linklisting'):
    
    for link in tag.find_all('a', href = True):
        pic = (link['href'])
        pic_list += [pic]
#background_pic = pic_list[0]





#url = background_pic
url = 'http://i.imgur.com/cMn17t9.png'
response = requests.get(url, stream=True)
with open('img.png', 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)
del response

import ctypes
SPI_SETDESKWALLPAPER = 20 
ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, "img.png" , 0)
