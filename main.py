# -*- coding: utf-8 -*-
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


# def save(img, filename='temp', path='dota_abaddon'):
#     fpath = os.path.join(path, filename)
#     isExists = os.path.exists(path)
#
#     # 判断结果
#     if not isExists:
#         os.makedirs(path)
#     with open(fpath, 'wb+') as  f:
#         print('output:', fpath)
#         f.write(img)
#
# def savestr(str, filename='temp', path='dota_abaddon'):
#     fpath = os.path.join(path, filename)
#     isExists = os.path.exists(path)
#
#     # 判断结果
#     if not isExists:
#         os.makedirs(path)
#     with open(fpath, 'a+', encoding='UTF-8') as  f:
#         print('output:', fpath)
#         f.write(str)
#
# def save_image(image_url):
#     resp = requests.get(image_url)
#     page = resp.content
#     filename = image_url.split('www.dotabuff.com/')[-1]
#     save(page, image_url)

def getHeroElementXPath():
    return '/html/body/div[2]/div[3]/div[1]/div[2]/table/tbody/tr'

def getHeroNameXPath():
    return './/span'#''/html/body/div[2]/div[3]/div[1]/div[2]/table/tbody/tr[' + str(index +1) + ']/td[1]/span'

def crawl(url):
    resp = requests.get(url, headers=headers)
    page = resp.content
    root = html.fromstring(page)
    HeroElements = root.xpath(getHeroElementXPath())

    dic = dict()
    #dic = [['name', 'best_versus', 'worst_versus', 'best_teammate']]
    for heroElement in HeroElements:
        herourl = heroElement.get('onclick').split('\'')[1]
        herourl = 'http://www.dotamax.com' + herourl
        chineseName = heroElement.xpath(getHeroNameXPath())[0].text#[0].text
        BestVersus, WorstVersus, BestTeammate = crawlHero(herourl)
        dic[chineseName] = [BestVersus, WorstVersus, BestTeammate]
        print ('crawl hero' + chineseName + 'finished')
    savefile.saveXML(dic)
    savefile.saveCSV(dic)
def crawlHero(url):
    resp = requests.get(url, headers=headers)
    page = resp.content
    root = html.fromstring(page)
    BestVersusElements = root.xpath('/html/body/div[2]/div[3]/div[1]/div[2]/table[3]/tbody/tr/td[1]/span')
    BestVersus = []
    for heroElement in BestVersusElements:
        chineseName = heroElement.text
        BestVersus += [chineseName]
    WorstVersusElements = root.xpath('/html/body/div[2]/div[3]/div[1]/div[2]/table[4]/tbody/tr/td[1]/span')
    WorstVersus = []
    for heroElement in WorstVersusElements:
        chineseName = heroElement.text
        WorstVersus += [chineseName]
    BestTeammateElements = root.xpath('/html/body/div[2]/div[3]/div[1]/div[2]/table[5]/tbody/tr/td[1]/span')
    BestTeammate = []
    for heroElement in BestTeammateElements:
        chineseName = heroElement.text
        BestTeammate += [chineseName]
    return BestVersus, WorstVersus, BestTeammate

if __name__ == '__main__':
    url = 'http://www.dotamax.com/player/hero/'

    crawl(url)
