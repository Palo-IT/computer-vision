import requests


def image_search(file_path):
    search_url = 'http://www.google.hr/searchbyimage/upload'
    multipart = {'encoded_image': (file_path, open(file_path, 'rb')), 'image_content': ''}
    response = requests.post(search_url, files=multipart, allow_redirects=False)
    fetch_url = response.headers['Location']
    return fetch_url
