import pytest
import RestRCI
import logging
import time
import json
import os
import sys

# @pytest.fixture(scope='module')
# def log():
logging.basicConfig(filename=r"C:\Users\vs6993\PycharmProjects\restrci_automation\rest_rci.log",level=logging.DEBUG)


@pytest.fixture(scope='session',autouse=True)
def api():
    '''
    pytest RESTRCI server fixture that can be used in all test scripts to get access to server instance.
    '''
    api=RestRCI.rest()
    print(api.url)
    f = open("restRCI_summary.txt","w")
    f.write(time.asctime( time.localtime(time.time()) ))
    return api



