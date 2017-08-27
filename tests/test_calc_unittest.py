import unittest
from selenium import webdriver
from utils.pom import *
from utils.utils import Utils


class CalcPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = 'http://adam.goucher.ca/parkcalc/'
        self.driver.get(self.url)

    def tearDown(self):
        self.driver.quit()

    def test_1(self):
        page_1 = CalcPage(self.driver, self.url)
        page_1.ChooseLot('EP')
        page_1.ChooseEntryTimeDate('03:00', 'PM', '09/27/2017', type_in=False)
        page_1.ChooseExitTimeDate('04:00', 'PM', '09/28/2017', type_in=False)
        page_1.Calculate()
        self.assertEqual(Utils(self.driver).price(), '$ 4.00')

if __name__ == '__main__':
    unittest.main()