import webbrowser

# https://nhentai.net/search/?q=hello&sort=popular-today

def search_nhentai(query, sort=None):
    nhentai_url = "https://nhentai.net/search/?q=" + query
    if(sort!=None):
        validate_tags = ('popular-today', 'popular-week', 'popular') #tuple to prevent modification
        if sort not in validate_tags:
            raise ValueError("sort popularity unavailable")
        nhentai_url += "&sort=" + sort
    return webbrowser.open(nhentai_url)

search_nhentai('mogeko')