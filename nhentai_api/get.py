from bs4 import BeautifulSoup
import requests
import urllib
import json
import random

# get html json and parse it
# optionally prettify return to organize the text
def html_from_url(query: str):
    nhentai_url = "https://nhentai.net/" + query
    r = requests.get(nhentai_url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

# get cover of manga
# first find all classes with lazyload (which hold images)
# then retrieve image with 'cover' in url
def cover_from_manga(query: str):
    manga = html_from_url('g/' + query)
    images = manga.findAll(class_="lazyload") 
    for image in images:
        if('cover' in image['data-src']):
            return image['data-src']
    return None

# get english title of manga
# first find header with title class
# then find span with pretty class
def en_title_of_manga(query: str):
    manga = html_from_url('g/' + query)
    class_title = manga.find("h1", {"class": "title"})
    english_title = class_title.find("span", {"class": "pretty"}).getText()
    return english_title

# same as above but japanese
def jp_title_of_manga(query: str):
    manga = html_from_url('g/' + query)
    class_title = manga.find("h2", {"class": "title"})
    jp_title = class_title.find("span", {"class": "pretty"}).getText()
    return jp_title

# get array of tags/parodies/etc of a manga
# first get html, then find the section for tags
# find all the tags by <a>

# iterate through the <a> received, and if '/tag/'
# exists in the iteration, append to array
def tags_of_manga(query: str, tag_type: str):
    validate_tags = ('parody', 'tag', 'artist', 'group', 'language', 'category') #tuple to prevent modification
    if tag_type not in validate_tags:
        raise ValueError("Tag unavailable")

    manga = html_from_url('g/' + query)
    section_tags = manga.find("section", {"id": "tags"})
    tags_section = section_tags.findAll("a")

    tags = []
    tag = f'/{tag_type}/'

    for tag_url in tags_section:
        if(tag in tag_url["href"]):
            temp = tag_url.find(class_="name")
            tags.append(temp.text)
    
    return tags

# get manga id in gallery
def id_of_manga(query: str):
    manga = html_from_url('g/' + query)
    gallery_id = manga.find("h3", {"id": "gallery_id"})
    return gallery_id.text

# get image from manga
# query must be string to get query
def image_of_manga_page(query: str):
    manga = html_from_url('g/' + query)
    section = manga.find("section", {"id":"image-container"})
    image = section.find("img")
    return image['src']

# get random image from the manga
# first analyze all thumbnails
# get redirect href for all of them
# choose one randomly from array
# plug result into get_image_of_manga_page
def random_image_of_manga(query):
    manga = html_from_url('g/' + query)
    thumbnail_container = manga.find("div", {"id": "thumbnail-container"})
    all_thumbs = thumbnail_container.findAll(class_="thumb-container")
    thumbs = []
    for thumb in all_thumbs:
        thumb_href = thumb.find("a")
        thumbs.append(thumb_href['href'].replace('/g/', ''))
    
    random_id = random.choice(thumbs)
    return image_of_manga_page(random_id)

# get all images
# first analyze all thumbnails
# get redirect href for all of them
# plug id value into 
def all_images_of_manga(query):
    manga = html_from_url('g/' + query)
    thumbnail_container = manga.find("div", {"id": "thumbnail-container"})
    all_thumbs = thumbnail_container.findAll(class_="thumb-container")
    images = []
    for thumb in all_thumbs:
        thumb_href = thumb.find("a")
        image = image_of_manga_page(thumb_href['href'].replace('/g/', ''))
        images.append(image)
    
    return images

# returns set of gallery objects
# these gallery objects refer to the cover and title of a manga
# shown by the category and its type
def gallery_group_info_by_category(category, type):
    validate_tags = ('parody', 'character', 'tag', 'artist', 'group') # tuple to prevent modification
    if category not in validate_tags:
        raise ValueError("type unavailable")
    html = html_from_url(category + "/" + type + "/")
    gall_container = html.find("div", {"id": "content"})
    each_gall_group = gall_container.findAll("div", {"class": "gallery"})

    collection = []

    for gall in each_gall_group:
        image = gall.find("a")['href'].replace('/g/','')
        image_cover = cover_from_manga(image)
        image_title = gall.find("div", {"class": "caption"}).getText()
        image_info = {image_cover, image_title}
        
        collection.append(image_info)
    
    return collection

# returns set of gallery objects
# these gallery objects refer to the cover and title of a manga
# shown by the category and its type
def gallery_group_info(query, sort=None):
    append = "search/?q=" + query
    if(sort!=None):
        validate_tags = ('popular-today', 'popular-week', 'popular') # tuple to prevent modification
        if sort not in validate_tags:
            raise ValueError("sort popularity unavailable")
        append += "&sort=" + sort

    html = html_from_url(append)
    gall_container = html.find("div", {"id": "content"})
    each_gall_group = gall_container.findAll("div", {"class": "gallery"})

    collection = []

    for gall in each_gall_group:
        image = gall.find("a")['href'].replace('/g/','')
        image_cover = cover_from_manga(image)
        image_title = gall.find("div", {"class": "caption"}).getText()
        image_info = {image_cover, image_title}
        
        collection.append(image_info)
    
    return collection

# goal is to limit the amount of groups which print from the collection above
# so print ten groups. if the person wants more groups, print ten more.
# try to optimize the function to print pictures faster. so perhaps dont return the entire
# collection yet
def loop_thru_array():
    red = range(100)
    yes = True
    while(yes)
        for i in red:
            print(i)
            if(indexOf(i) === red%10)

loop_thru_array()