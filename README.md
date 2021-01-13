# H-Bot [Version 1.0]

The current goal of this project is to create APIs for manga websites which don't have a web-scraper implemented for them. These APIs will then store the returned values of their functions into a private database.

## nhentai

Here are the readily available functions for over 335000 galleries to scrape.

`def html_from_url(query: str)`

Gets the HTML from the base nhentai URL and a query given to it. It parses the file and returns it as a JSON.

`def cover_from_manga(query: str)`

Returns the cover of a manga. First finds all classes with lazyload (which holds images) and retrieves the image with 'cover' in the URL

`def en_title_of_manga(query: str)`

Returns English title of manga. First finds the header with a title class, then finds the span with the pretty class.

`def jp_title_of_manga(query: str)`

Same as above, but for Japanese titles

`def tags_of_manga(query: str, tag_type: str)`

Returns the array of tags/parodies/etc of a manga. First gets the html, then finds the section for tags, and finds all the tags by <a>

Iterates through the <a> received, and if '/tag/' exists in the iteration, append to array

`def id_of_manga(query: str)`

Returns manga ID in gallery

`def image_of_manga_page(query: str)`

Returns image from manga. Query must be a string to get the result.

`def random_image_of_manga(query)`

Gets a random image from the manga. First analyzes all thumbnails. Then gets the redirect href for all of them. Then, it chooses one randomly from the array, and plugs the result into `image_of_manga_page`.

`def all_images_of_manga(query)`

Returns all the images of the manga. First analyzes all the thumbnails. Then gets the redirect href for all of them. For every thumbnail in the all_thumbs array, the id is appended inside `image_of_manga_page`.

`def gallery_group_info_by_category(category, type)`

(INCOMPLETE/SLOW) Returns a set of gallery objects, referring to the cover and title of a manga dependent on the category and its type.

`def gallery_group_info(query, sort=None)`

(INCOMPLETE/SLOW) Returns set of gallery objects, referring to the cover and its title, using query and sort.
