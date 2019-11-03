import requests
from abc import *

class Kakao_api:
    def __init__(self):
        self.api_key = 'KAKAO_API'

        self.headers = {
            'Authorization': 'KakaoAK '+self.api_key
        }

    def get_json(self, url, payload):
        return requests.get(url, headers=self.headers, params=payload).json()

    def post_json(self, url, data=None, file=None):
        return requests.post(url, headers=self.headers, data=data, files=file).json()

    @abstractmethod
    def url_maker(self):
        pass