from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote_plus
import requests, re, os

class getThumbnail:
    def getThumbnail(self, name):
        baseurl="https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
        url = baseurl + quote_plus(name)
        html = requests.get(url, verify=False)
        soup = BeautifulSoup(html.text, 'html.parser')
        html.close()

        data_list = soup.find_all(class_='thumb')
        thumb = data_list[1].find('img')
        thumb_src = thumb['src']
        if thumb_src.find("&type")>-1:
            thumb_src=thumb_src[0:thumb_src.find("&type")]

        return thumb_src