import bs4
import requests
import shutil
import os
import random


# GOOGLE_IMAGE = \
#     'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'


def extract(data, quantity):

    GOOGLE_IMAGE = \
    'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'

    URL_input = GOOGLE_IMAGE + 'q=' + data
    print('Fetching from url =', URL_input)
    URLdata = requests.get(URL_input)
    soup = bs4.BeautifulSoup(URLdata.text, "html.parser")
    ImgTags = soup.find_all('img')
    i = 0
    print('Please wait..')
    random.shuffle(ImgTags)

    for link in ImgTags:
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
            if i==4:  return images  #return 4rd image link
            

        except:
            pass
    print('\t\t\t Downloaded Successfully..\t\t ')

if __name__ == '__main__':
    data = input('What are you looking for? ')
    quantity = int(input('How many photos you want? '))
    extract(data, quantity)