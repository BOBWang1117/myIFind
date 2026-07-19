"""
myStock - A stock market analysis and tracking application.

This module serves as the entry point for the myStock application,
handling initialization and orchestration of the main program flow.
"""
import configparser

from sdk.basic.ifind_api import IFindAPI

config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')

def main():
    """
    This is the entry point for the myStock application.
    :return:
    """
    refresh_token = config.get('DEFAULT', 'refresh_token')

    iFind_api = IFindAPI(refresh_token=refresh_token) # pylint: disable=invalid-name
    response = iFind_api.access_token
    print(response)

    print(config.get('DEFAULT', 'refresh_token'))

if __name__ == "__main__":
    main()
