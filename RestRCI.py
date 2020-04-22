"""
rest api automation: this automation code is for fx9600 series readers
author : vs6993
"""

import requests
import time
import os
#import jsonschema
import json
import logging
from configparser import ConfigParser
import pytest


character = "-"   # character to be used as spliter to seperate commands

config = ConfigParser()
config.read("setting.ini")

logging.basicConfig(filename=os.getcwd()+r"\rest_rci.log",level=logging.INFO,filemode='w')
log = logging.getLogger()

ErrorTypes = {
    0: 'No Error',
    1: 'Bad message',
    2: 'CRC error',
    3: 'Buffer full',
    4: 'Response too big',
    5: 'Memory overrun',
    6: 'Reader too cold',
    7: 'Reader hot',
    8: 'Reader too hot',
    20: 'Command not supported',
    21: 'Field not supported',
    22: 'Field value not supported',
    23: 'Field value changed',
    24: 'GPIO toggle value the same',
    25: 'GPIO not settable',
    26: 'Trigger not an input switch',
    30: 'SpotProfiles full',
    31: 'SpotProfile error',
    32: 'Illegal SpotProfile',
    33: 'ThisTag timeout',
    34: 'Spot error',
    40: 'ReadZones full',
    41: 'ReadZone start error',
    42: 'ReadZone definition error',
    1001: 'GPIO apis failed',
    1002: 'Unhandled Exception while processing request',
    1003: "Singulation settings GET/SET failed",
    1004: "AntennaConfig settings GET/SET failed",
    1005: "No Tag URL registered",
    1006: "Unknown exception while posting tags",
    1007: "Add prefilter API failed"
}

class rest:
    global ip, endpoint, protocal, url

    def __init__(self):
        '''
        setting protocal , ip , endpoint and URL
        '''
        self.con = ConfigParser()
        self.con.read("setting.ini")
        self.ip = self.con.get('config', 'ip')
        self.endpoint = self.con.get('config', 'endpoint')
        self.protocal = self.con.get('config', 'protocal')
        # self.header = self.con.get('config','')
        self.url = self.protocal + "://" + self.ip + "/" + self.endpoint
        self.y = time.localtime()

    # def validate(self,response , command):
    #
    #     output = json.loads(response.text)
    #
    #     command_field = command.get["Cmd"]
    #     try:
    #         schema=open("C:\\Users\\vs6993\PycharmProjects\\restrci_automation\\schema\\GetInfo.json",'r')
    #         schema= json.dumps(schema.read())
    #     except FileNotFoundError as e:
    #         print(e)
    #
    #
    #     if jsonschema.validate(output,schema):
    #         return True
    #     else:
    #         return False
    #
    #
    # def GetERROR(json_resp):
    #     value=json_resp["ErrID"]
    #     return value, ErrorTypes[value]
