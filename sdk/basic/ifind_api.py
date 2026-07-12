import requests
import json

from datetime import datetime

class IFind_API:
    def __init__(self, refresh_token):
        self.base_url = 'https://quantapi.51ifind.com'
        self.refresh_token = refresh_token
        self.access_token = None

        self.__get_access_token()

    def __get_access_token(self):
        response = self.get_api_v1_get_access_token()
        if response.status_code == 200:
            data = json.loads(response.content)
            expired_time = data['data']['expired_time']
            if datetime.strptime(expired_time, '%Y-%m-%d %H:%M:%S') > datetime.now():
                self.access_token = data['data']['access_token']
            else:
                response = self.post_api_v1_update_access_token()
                if response.status_code == 200:
                    data = json.loads(response.content)
                    self.access_token = data['data']['access_token']
        else:
            raise Exception("Refresh token expired or invalid")

    def get_api_v1_get_access_token(self):
        path = '/api/v1/get_access_token'
        url = "{}{}".format(self.base_url, path)

        headers = {"Content-Type": "application/json", "refresh_token": self.refresh_token}
        response = requests.get(url=url, headers=headers)
        return response
    
    def post_api_v1_update_access_token(self):
        path = '/api/v1/update_access_token'
        url = "{}{}".format(self.base_url, path)

        headers = {"Content-Type": "application/json", "refresh_token": self.refresh_token}
        response = requests.post(url=url, headers=headers)
        return responsea