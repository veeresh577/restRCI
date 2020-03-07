import requests
import time
import random
import logging
import json

logging.basicConfig(filename=r"C:\Users\vs6993\PycharmProjects\restrci_automation\stress_testing.log",level=logging.INFO,filemode='w')
log = logging.getLogger()

log.info("************stress test case **********")

ip = "10.17.131.131"
url = "http://"+ip+"/restrci"
header = [('Content-type', 'application/json')]
t = time.localtime()
y = time.localtime()
time.sleep(60)

exce=0

while not ( t.tm_hour == y.tm_hour - 1 and t.tm_min == y.tm_min):
    try:
        y=time.localtime()
        stop_condition = random.randrange(1,4,1)
        if stop_condition == 1:
            stop_value = random.randrange(3,20,1)
        elif stop_condition == 2:
            stop_value = random.randrange(500,6000,100)
        else:
            stop_value = random.randrange(3,6,1)

        payload={"Cmd": "_GetTags", "_StopCondition": stop_condition, "_StopValue": stop_value}
        payload=json.dumps(payload)

        resp = requests.post(url=url, data = payload)
        log.info(payload)
        log.info(resp.text + '\n')

    except requests.exceptions.ConnectionError as e:
        print(e)
        log.info(e)
        exce = exce + 1
    except Exception as e:
        print(e)
        log.info(e)

print("completed")
log.info("completed")



