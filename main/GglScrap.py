'''
Author - Aditya Mangal
Date - 27 october 2020
Purpose - Python mini task

#used to scrape images from google 

'''

import bs4
import requests
import shutil
import os
from pprint import pprint

GOOGLE_IMAGE =\
        'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'
# print(GOOGLE_IMAGE)
# GOOGLE_IMAGE=os.path.normpath(GOOGLE_IMAGE)
# print(GOOGLE_IMAGE)
def extract(data, quantity):
    URL_input = GOOGLE_IMAGE + 'q=' + data
    print('Fetching from url =', URL_input)
    URLdata = requests.get(URL_input)
    soup = bs4.BeautifulSoup(URLdata.text, "html.parser")

    print(soup)


    ImgTags = soup.find_all('img')
    print("-------------------")
    print(ImgTags)

    i = 0
    pprint('Please wait..')
    while i < quantity:
        print(f"i is {i}")
        for link in ImgTags:
            if i==quantity:
                break
            try:
                images = link.get('src')
                ext = images[images.rindex('.'):]
                if ext.startswith('.png'):
                    ext = '.png'
                elif ext.startswith('.jpg'):
                    ext = '.jpg'
                elif ext.startswith('.jfif'):
                    ext = '.jfif'
                elif ext.startswith('.com'):
                    ext = '.jpg'
                elif ext.startswith('.svg'):
                    ext = '.svg'
                data = requests.get(images, stream=True)
                filename = str(i) + ext
                with open(filename, 'wb') as file:
                    shutil.copyfileobj(data.raw, file)
                i += 1
            except:
                pass
    print('\t\t\t Downloaded Successfully..\t\t ')


data = input('What are you looking for? ')
quantity = int(input('How many photos you want? '))
extract(data, quantity)