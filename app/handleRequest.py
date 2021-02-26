"""
Handle user Requests

Authors: Majeed Malik
"""

from newspaper import Article

def process_url(url, params):
    """Handle request from user"""

    article = Article(url)
    article.download()
    article.parse()
    element_to_return = {}

    if 'title' in params:
        title = article.title
        element_to_return['title'] = title

    if 'text' in params:
        text = article.text
        element_to_return['text'] = text

    if 'author' in params:
        author = article.authors
        element_to_return['author'] = author
    
    if 'publishDate' in params:
        publishDate = article.publish_date
        element_to_return['publishDate'] = publishDate
    
    if 'keywords' in params:
        keywords = article.keywords
        element_to_return['keywords'] = keywords

    for element in element_to_return.keys():
        if element_to_return[element] == None or element_to_return[element] == []:
            element_to_return[element] = ""
        if type(element_to_return[element]) == list:
           element_to_return[element] = ''.join(element_to_return[element])
    image = article.top_image
    element_to_return['image'] = image
    
    return element_to_return
