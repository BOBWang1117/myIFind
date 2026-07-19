"""
Utility Function Module
Provide general-purpose utility functions, including features such as scheduled tasks and decorators.
"""
import configparser

from sdk.basic.ifind_api import IFindAPI


class Tools:
    """
    Encapsulates GET/POST request methods for the IFind data service.
    """
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini', encoding='utf-8')
        self.refresh_token = self.__get_refresh_token()
        self.iFind_api = IFindAPI(self.refresh_token)  # pylint: disable=invalid-name

    def __get_refresh_token(self):
        """
        The function to obtain the iFind token
        """
        refresh_token = self.config.get('DEFAULT', 'refresh_token')

        return refresh_token

    def get_codes(self):
        """
        The function to obtain the iFind stock codes
        """
        codes = self.config.get('INFO', 'codes')

        return codes

    def get_ths_fund_inner_short_name_fund(self, codes):
        """
        The function to obtain the ths fund inner short name fund
        """
        response = self.iFind_api.get_api_v1_basic_data_service(codes)
        ths_fund_inner_short_name_fund = response.json()['tables'][0]['table']['ths_fund_inner_short_name_fund'][0]

        return ths_fund_inner_short_name_fund
