"""
myStock - A stock market analysis and tracking application.

This module serves as the entry point for the myStock application,
handling initialization and orchestration of the main program flow.
"""
from sdk.basic.tools import Tools

def main():
    """
    This is the entry point for the myStock application.
    :return:
    """
    tools = Tools()
    codes = tools.get_codes()
    name = tools.get_ths_fund_inner_short_name_fund(codes)
    print(f'code: {codes}, name: {name}')

if __name__ == "__main__":
    main()
