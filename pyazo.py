# -*- coding: utf-8 -*-
import requests


ENDPOINT = 'https://api.gyazo.com/api/{}'
UPLOAD_ENDPOINT = 'https://upload.gyazo.com/api/upload/{}'

IMAGES = ENDPOINT.format('images')
OEMBED = ENDPOINT.format('oembed')
UPLOAD = UPLOAD_ENDPOINT.format('')[:-1]
UPLOAD_WITH_BROWSER_SESSION = UPLOAD_ENDPOINT.format('easy_auth')


class MissingClientID(Exception):
    pass


class InvalidURLFormatError(Exception):
    pass


class Pyazo(object):
    def __init__(self,
                 access_token,
                 client_id=None,
                 client_secret=None):
        self.access_token = access_token
        self.client_id = client_id
        self.client_secret = client_secret

    def images(self, page=1, per_page=20):
        query = {
            'access_token': self.access_token,
            'page': page,
            'per_page': per_page
        }
        response = requests.get(IMAGES, data=query)
        return response.text

    def upload(self,
               image_path,
               referer_url=None,
               title=None,
               desc=None,
               created_at=None):
        files = {'imagedata': open(image_path, 'rb')}
        payload = {
            'access_token': self.access_token,
            'referer_url': referer_url,
            'title': title,
            'desc': desc,
            'created_at': created_at
        }
        response = requests.post(UPLOAD, data=payload, files=files)
        return response.text

    def delete(self, image_id):
        payload = {
            'access_token': self.access_token,
            'image_id': image_id
        }
        response = requests.delete(IMAGES + '/{}'.format(image_id),
                                   data=payload)
        return response.text

    def oembed(self, url):
        if not url.startswith('http://gyazo.com/'):
            raise InvalidURLFormatError()

        query = {'url': url}
        response = requests.get(OEMBED, data=query)
        return response.text

    def upload_easy_auth(self, image_url, referer_url, title=None):
        if not self.client_id:
            raise MissingClientID()

        payload = {
            'client_id': self.client_id,
            'image_url': image_url,
            'referer_url': referer_url,
            'title': title
        }
        response = requests.post(UPLOAD_WITH_BROWSER_SESSION, data=payload)
        return response.text
