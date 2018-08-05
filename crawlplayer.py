import os
import requests
from lxml import html
import savefile

headers = {'Host':'www.dotamax.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,en-US;q=0.7,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        #'Referer': 'http://neihanshequ.com/',
        'X-CSRFToken': 'e9b62faa6a962cdf92f1531b498fc771',
        'X-Requested-With': 'XMLHttpRequest',
        'Cookie': 'csrftoken=e9b62faa6a962cdf92f1531b498fc771; tt_webid=6486401443292186126; uuid="w:c07f437659474cc1a7cfd052d9985b37"; Hm_lvt_3280fbe8d51d664ffc36594659b91638=1511848146,1512200937,1512371475,1514373568',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache'}

def getXPath():
    return
def crawlplayer(url):
    resp = requests.get(url, headers=headers)
    page = resp.content
    root = html.fromstring(page)
    HeroElements = root.xpath(getXPath())

if __name__ == '__main__':
    url = 'http://www.dotamax.com/player/hero/'
    crawlplayer(url)
