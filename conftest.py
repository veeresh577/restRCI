import pytest
import RestRCI
import logging
import time
import datetime
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

    return api

def pytest_sessionstart():
    global suite_start_time

    suite_start_time = datetime.datetime.now()
    timestamp = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')

    return True

test_passed=test_failed=test_skipped=0
def pytest_runtest_logreport(report):
    '''Consolidated data for summary.txt'''
    global dir_name
    global test_passed, test_failed, test_skipped,result_dict
    if report.when == 'call' and report.outcome == 'passed':
        test_passed += 1
    if report.when == 'call' and report.outcome == 'failed':
        test_failed +=1
    if report.outcome == 'skipped':
        test_skipped +=1


def pytest_sessionfinish():
    '''Fill data in REST_RCI_api_summary.txt'''
    global test_passed, test_failed, test_skipped, suite_start_time
    total = test_passed + test_failed + test_skipped

    delta =  datetime.datetime.now() - suite_start_time

    try:
        with open("REST RCI api summary.txt", "a+") as f:
            t=time.localtime()
            f.write('\nDate = : '+str(t.tm_mday)+'/'+str(t.tm_mon)+'/'+str(t.tm_year)+ '   Time = :' + str(t.tm_hour) + '.' + str(t.tm_min))
            f.write('\n\t \t \t \ttotal  passed  failed  skipped')
            f.write('\nTest Count   = ' + '\t' + str(total) \
                    + '\t   ' + str(test_passed) \
                    + '\t   '  + str(test_failed) \
                    + '\t   ' + str(test_skipped) + "\n")

            f.write("Pass Test case Ratio = " + str(round(float(test_passed)/total*100,2)) + ' % \n')
            f.write("Fail Test case Ratio = " + str(round(float(test_failed)/total*100,2)) + ' % \n')
            f.write("Skip Test case Ratio = " + str(round(float(test_skipped)/total*100,2)) + ' % \n\n\n')

            f.write("REST RCI API Automation Total time taken = " + str(delta))
            f.write('\n-------------------------------------------------------------------------------')

    except ZeroDivisionError:
            pass





