from bs4 import BeautifulSoup as bs

import requests
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-tag', help = "Desired Tag")
parser.add_argument('-pop', help = "Sort by popularity")
parser.add_argument('-r', help = "Get random doujinshi")

print("Enter url: ")
url = input()

content = requests.get(url).content
print(content)

soup = bs(content,'lxml')

image_tags = soup.findAll('img')

titles = soup.findAll('div', {'class': 'caption'})

for image_tag in image_tags:
    print(image_tag.get('src'))

for title in titles:
    print(title.string)
