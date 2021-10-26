from urllib.request import urlopen

from bs4 import BeautifulSoup as BS

from hello_doc_proj.celery import app

@app.task
def num_apperances_of_tag(url):
    soup = BS(urlopen(url))
    dictionary = {'tags': {}}
    for tag in soup.findAll():
        try:
            dictionary['tags'][tag.name] += 1
        except KeyError:
            dictionary['tags'][tag.name] = 1
    if 'html' in dictionary['tags'].keys():
        return dictionary
    return {'response': 'It is not a html site'}
