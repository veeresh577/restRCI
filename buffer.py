# from configparser import ConfigParser
#
# config=ConfigParser()
#
# config.read("setting.ini")
# print(config.sections())
#
#
# readerInfo = config.get('commands','GetreaderInfo')
# print(readerInfo)
# import json
# try:
#     schema=open("C:\\Users\\vs6993\PycharmProjects\\restrci_automation\\schema\\GetInfo.json",'r')
#     schema= json.dumps(schema.read())
#     print(schema)
# except FileNotFoundError as e:
#             print(e)

l=[[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
for i in l:
    print(i)
