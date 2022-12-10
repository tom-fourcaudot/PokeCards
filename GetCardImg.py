import urllib.request as ur
from bs4 import BeautifulSoup as bs

def getImg(url:str)->str:
    page = ur.urlopen(url)
    soup_obj = bs(page, 'html.parser')
    for img in soup_obj.find_all('img', attrs={"class":"is-front"}, ) :
        if not 'lazy' in img.get('class'):
            return img.get('src')
    return ''