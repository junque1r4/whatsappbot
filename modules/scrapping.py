from bs4 import BeautifulSoup
import requests
import secrets
from random import randint
def meme(y):
    site = requests.get(f'https://www.ahnegao.com.br/pag/{y}').content
    soup = BeautifulSoup(site, 'html.parser')
    images = []

    for img in soup.findAll('img'):
        if 'https' and 'uploads' in str(img):
            if 'logo-466x156' and 'logom' in str(img):
                pass
            else:
                images.append(img.get('src'))    
    images.remove('https://www.ahnegao.com.br/wp-content/uploads/2021/01/logo-466x156.png')
    try:
        return images[randint(0,5)]
    except:
        return meme(y)