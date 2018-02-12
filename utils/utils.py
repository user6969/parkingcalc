from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from locators import *
from time import sleep


TIME_OUT = 10
MONTH = {'01': 'January',
         '02': 'February',
         '03': 'March',
         '04': 'April',
         '05': 'May',
         '06': 'June',
         '07': 'July',
         '08': 'August',
         '09': 'September',
         '10': 'October',
         '11': 'November',
         '12': 'December'
        }


class Utils(object):

    def __init__(self, driver):
        self.driver = driver

    def select_lot(self, lot):
        menu = self.driver.find_element(*CalcPageLocators.Lot)
        menu.click()
        options = self.driver.find_elements(*CalcPageLocators.Options)
        for option in options:
            if option.get_attribute('value') == lot:
                option.click()

    def select_entry_time(self, time):
        el = self.driver.find_element(*CalcPageLocators.EntryTime)
        el.clear()
        el.send_keys(time)

    def select_entry_ampm(self, ampm):
        if ampm == 'AM':
            els = self.driver.find_elements(*CalcPageLocators.EntryAMPM)
            els[0].click()
        else:
            els = self.driver.find_elements(*CalcPageLocators.EntryAMPM)
            els[1].click()

    def select_entry_date(self, date, type_in):
        if type_in:
            el = self.driver.find_element(*CalcPageLocators.EntryDate)
            el.clear()
            el.send_keys(date)
        else:
            month_num = date.split('/')[0]
            day = date.split('/')[1]
            year = date.split('/')[2]
            self.select_entry_date_from_date_picker(MONTH.get(month_num), day, year)

    def select_entry_date_from_date_picker(self, month, day, year):
        window_before = self.driver.window_handles[0]
        els = self.driver.find_elements(*CalcPageLocators.DatePicker)
        els[1].click()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        self.driver.maximize_window()
        self.select_month(month)
        self.select_year(year)
        self.select_day(day)
        self.driver.switch_to.window(window_before)

    def select_exit_date_from_date_picker(self, month, day, year):
        window_before = self.driver.window_handles[0]
        els = self.driver.find_elements(*CalcPageLocators.DatePicker)
        els[2].click()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        self.select_month(month)
        self.select_year(year)
        self.select_day(day)
        self.driver.switch_to.window(window_before)

    def select_exit_time(self, time):
        el = self.driver.find_element(*CalcPageLocators.ExitTime)
        el.clear()
        el.send_keys(time)

    def select_exit_ampm(self, ampm):
        if ampm == 'AM':
            els = self.driver.find_elements(*CalcPageLocators.ExitAMPM)
            els[0].click()
        else:
            els = self.driver.find_elements(*CalcPageLocators.ExitAMPM)
            els[1].click()

    def select_exit_date(self, date, type_in):
        if type_in:
            el = self.driver.find_element(*CalcPageLocators.ExitDate)
            el.clear()
            el.send_keys(date)
        else:
            month_num = date.split('/')[0]
            day = date.split('/')[1]
            year = date.split('/')[2]
            self.select_exit_date_from_date_picker(MONTH.get(month_num), day, year)

    def calculate(self):
        el = self.driver.find_element(*CalcPageLocators.Calculate)
        el.click()

    def price(self):
        try:
            els = self.driver.find_elements(*CalcPageLocators.Cost)
            cost = els[0].text
            #duration = els[1].text
            return cost
        except NoSuchElementException:
            el = self.driver.find_element(*CalcPageLocators.Error)
            error = el.text
            return error

    def select_month(self, month):

        select = Select(self.driver.find_element(*PickDateLocators.Month))
        select.select_by_visible_text(month)

    def select_year(self, year):
        els = self.driver.find_elements(*PickDateLocators.Year)
        if els[1].text == year:
            pass
        elif int(els[1].text) > int(year):
            while int(els[1].text) > int(year):
                els[2].click()
        elif int(els[1].text) < int(year):
            while int(els[1].text) < int(year):
                els[0].click()
        else:
            pass #TODO handling

    def select_day(self, day):
        el = self.driver.find_element_by_link_text(day)
        el.click()

    def edit(self, field):
        pass

    def click(self, location):
        pass
