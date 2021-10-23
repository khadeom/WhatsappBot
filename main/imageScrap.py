import os, urllib.request, json # json for pretty output
from serpapi import GoogleSearch


def get_google_images():
    params = {
      "api_key": os.getenv("11f2777e6f0286728257a03955a73813"),
      "engine": "google",
      "q": "pexels cat",
      "tbm": "isch"
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    # print(json.dumps(results['suggested_searches'], indent=2, ensure_ascii=False))
    print(json.dumps(results['images_results'], indent=2, ensure_ascii=False))

    # -----------------------
    # Downloading images

    for index, image in enumerate(results['images_results']):

        print(f'Downloading {index} image...')
        
        opener=urllib.request.build_opener()
        opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582')]
        urllib.request.install_opener(opener)

        urllib.request.urlretrieve(image['original'], f'SerpApi_Images/original_size_img_{index}.jpg')


get_google_images()



'''
Suggested search results:
[
  {
    "name": "wallpaper",
    "link": "https://www.google.com/search?q=minecraft+shaders+8k+photo&tbm=isch&chips=q:minecraft+shaders+8k+photo,online_chips:wallpaper:M78_F4UxoJw%3D&hl=en-US&sa=X&ved=2ahUKEwibusKPuvjxAhWFEt8KHbN0CBUQ4lYoAHoECAEQEQ",
    "chips": "q:minecraft+shaders+8k+photo,online_chips:wallpaper:M78_F4UxoJw%3D",
    "serpapi_link": "https://serpapi.com/search.json?chips=q%3Aminecraft%2Bshaders%2B8k%2Bphoto%2Conline_chips%3Awallpaper%3AM78_F4UxoJw%253D&device=desktop&engine=google&google_domain=google.com&q=minecraft+shaders+8k+photo&tbm=isch",
    "thumbnail": "https://serpapi.com/searches/60fa52ca477c0ec3f75f0d3b/images/3868309500692ce40237282387fb16587c67c8a9bb635eefe35216c182003a4d.jpeg"
  }
...
]

--------------------------

Image results:
[
  {
    "position": 1,
    "thumbnail": "https://serpapi.com/searches/60fa52ca477c0ec3f75f0d3b/images/07dc65d29a3e1094e9c1551efe12324ee8387d268cf2eec92bf0eaed1550eecb.jpeg",
    "source": "reddit.com",
    "title": "8k Minecraft + Shaders: Minecraft",
    "link": "https://www.reddit.com/r/Minecraft/comments/6iamxa/8k_minecraft_shaders/",
    "original": "https://external-preview.redd.it/mAQWN2kUYgFS3fgm6LfYo37AY7i2e_YY8d83_1jTeys.jpg?auto=webp&s=b2bad0e23cbd83426b06e6a547ef32ebbc08e2d2"
  }
...
]
'''