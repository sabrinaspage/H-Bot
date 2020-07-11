from bs4 import BeautifulSoup as bs

import urllib

import requests
import os
import argparse



parser = argparse.ArgumentParser()
parser.add_argument('-tag', help = "Desired Tag")
parser.add_argument('-pop', help = "Sort by popularity")
parser.add_argument('-r', help = "Get random doujinshi")

url = "http://nhentai.net"

def setTag(tag):
    return url + "/tag/" + tag

print("Enter tag: ")
t = input()

content = requests.get(setTag(t)).content
#print(content)

soup = bs(content,'lxml')

def retrieveSearch(soup):
    doujinsRef = soup.findAll('div',{'class': 'gallery'})
    doujins = []
    for doujinRef in doujinsRef:
        temp = {}
        temp['title'] = doujinRef.find('a').find('div',{'class','caption'}).string
        temp['thumbnail'] = doujinRef.find('a').find('img').get('data-src')
        temp['url'] = url + doujinRef.find('a').get('href')
        doujins.append(temp)
    return doujins

def getDoujinInfo(url):
    content = requests.get(url).content
    soup = bs(content,'lxml')
    infoJSON = {}

    titleTag = soup.find('h1',{'class','title'})
    before = titleTag.find('span',{'class','before'}).string
    pretty = titleTag.find('span',{'class','pretty'}).string
    after = titleTag.find('span',{'class','after'}).string
    infoJSON['title'] = before + " " + pretty + " " + after

    infoJSON['thumbnail'] = soup.find(id='cover').find('a').find('img').get('data-src')

    tagsTree = soup.find(id='tags').findAll('div',{'class','tag-container field-name'})
    tagsJSON = {}
    for tagType in tagsTree:
        tempArr = []
        taglist = tagType.find('span',{'class','tags'}).findAll('a')
        for tag in taglist:
            tempArr.append(tag.find('span',{'class','name'}).string)
        tagsJSON[tagType.text.strip().split(":")[0].lower()] = tempArr
    infoJSON['tagTypes'] = tagsJSON
    return infoJSON

list = retrieveSearch(soup)
print(list[0]['url'])

def getPage(url,pageNum):
    content = requests.get(url+str(pageNum)).content
    soup = bs(content,'lxml')
    return soup.find(id="image-container").find('a').find('img').get('src')

print(getPage(list[0]['url'],1))
"""
doujins = soup.findAll('div',{'class','gallery'})

for doujin in doujins:
    print(doujin.find('a').find('div',{'class','caption'}).string)
    print(doujin.find('a').find('img').get('data-src'))
    print(doujin.find('a').get('href'))
"""
