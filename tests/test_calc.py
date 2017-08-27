import pytest
from selenium import webdriver
from utils.pom import *
from utils.utils import Utils
from time import sleep

URL = 'http://adam.goucher.ca/parkcalc/'
ERROR = 'ERROR! YOUR EXIT DATE OR TIME IS BEFORE YOUR ENTRY DATE OR TIME'
FORMAT_ERROR = 'ERROR! ENTER A CORRECTLY FORMATTED DATE'


@pytest.yield_fixture(scope='session')
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.mark.parametrize('lot, entryTimeDate, exitTimeDate, result',
                        [('EP', ('03:00', 'PM', '08/25/2017', False),           # 1.Valid entry/exit
                                ('04:00', 'PM', '08/25/2017', False), '$ 4.00'),#   time/dates. Dates are selected via popup
                         ('EP', ('03:00', 'PM', '08/30/2017', True),            # 2.Entry date after
                                ('06:00', 'PM', '08/29/2017', False), ERROR),   #   exit date. Exit date is selected via popup
                         ('STP', ('03:00', 'PM', '09/02/2017', True),           # 3.Entry date after
                                 ('06:00', 'PM', '09/01/2017', True), ERROR),   #   exit date. Dates are typed in
                         ('LTS', ('02:00', 'PM', '08/30/2017', False),          # 4.Entry time after
                                ('01:00', 'PM', '08/29/2017', True), ERROR),    #   exit time.
                         ('EP', ('01:00', 'AM', '123/132/231', True),           # 5.Invalid date format
                                ('03:00', 'AM', '88/291/2167', True), ERROR),   #   Dates are typed in
                         ('LTG', ('AA:xx', 'AM', '08/28/2017', True),           # 6.Invalid time format
                                ('BB:yy', 'AM', '08/29/2017', True), ERROR),    #   Time is typed in
                         ('VP', ('01:00', 'AM', 'MM/DD/YYYY', True),            # 7.Invalid date format
                                ('02:00', 'AM', 'MM/DD/YYYY', True), FORMAT_ERROR) # Date is typed in
                         ]
                         )
def test_calc(browser, lot, entryTimeDate, exitTimeDate, result):
    browser.get(URL)
    calcpage = CalcPage(browser, URL)
    calcpage.ChooseLot(lot)
    calcpage.ChooseEntryTimeDate(*entryTimeDate)
    calcpage.ChooseExitTimeDate(*exitTimeDate)
    calcpage.Calculate()
    assert Utils(browser).price() == result

