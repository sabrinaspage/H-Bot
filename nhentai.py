from bs4 import BeautifulSoup as bs
import urllib
import requests

def retrieveSearch(tag):
    content = requests.get("http://nhentai.net/tag/" + tag).content
    soup = bs(content,'lxml')
    doujinsRef = soup.findAll('div',{'class': 'gallery'})
    doujins = []
    for doujinRef in doujinsRef:
        temp = {}
        temp['title'] = doujinRef.find('a').find('div',{'class','caption'}).string
        temp['thumbnail'] = doujinRef.find('a').find('img').get('data-src')
        temp['url'] = "http://nhentai.net" + doujinRef.find('a').get('href')
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

def getPage(url,pageNum):
    content = requests.get(url+str(pageNum)).content
    soup = bs(content,'lxml')
    return soup.find(id="image-container").find('a').find('img').get('src')

def getPages(url):
    pages = int(getDoujinInfo(url)['tagTypes']['pages'][0])
    temp = []
    for i in range(1,pages+1):
        temp.append(getPage(url,i))
    return temp



"""
doujins = soup.findAll('div',{'class','gallery'})

for doujin in doujins:
    print(doujin.find('a').find('div',{'class','caption'}).string)
    print(doujin.find('a').find('img').get('data-src'))
    print(doujin.find('a').get('href'))
"""
