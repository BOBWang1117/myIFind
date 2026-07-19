"""
Provide an interface encapsulation for interacting with the IFind data service.
"""
import json
from datetime import datetime
import requests


class IFindAPI:
    """
    Encapsulates GET/POST request methods for the IFind data service.
    """
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
            raise RuntimeError("Refresh token expired or invalid")

    def get_api_v1_get_access_token(self):
        """
        GET /api/v1/get_access_token
        """
        url = f"{self.base_url}/api/v1/get_access_token"
        headers = {"Content-Type": "application/json", "refresh_token": self.refresh_token}

        response = requests.get(url=url, headers=headers, timeout=10)
        return response

    def post_api_v1_update_access_token(self):
        """
        POST /api/v1/update_access_token
        """
        url = f"{self.base_url}/api/v1/update_access_token"
        headers = {"Content-Type": "application/json", "refresh_token": self.refresh_token}

        response = requests.post(url=url, headers=headers, timeout=10)
        return response

    def get_api_v1_basic_data_service(self, codes):
        """
        GET /api/v1/basic_data_service
        """
        url = f"{self.base_url}/api/v1/basic_data_service"
        headers = {"Content-Type": "application/json", "access_token": self.access_token}
        request_body = {
            "codes": codes,
            "indipara": [
                {
                    "indicator": "ths_fund_inner_short_name_fund"
                }
            ]
        }

        response = requests.post(url=url, headers=headers, data=json.dumps(request_body), timeout=10)
        return response
