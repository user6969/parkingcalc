from utils import Utils

class BasePage(object):

    def __init__(self, driver, base_url):
        self.url = base_url
        self.driver = driver
        self.actions = Utils(driver)

    def Edit(self, value):
        self.actions.edit(value)

    def Click(self, location):
        self.actions.click(location)

class CalcPage(BasePage):

    def choose_lot(self, lot):
        self.actions.select_lot(lot)

    def choose_entry_time_date(self, time, ampm, date, type_in):
        self.actions.select_entry_time(time)
        self.actions.select_entry_ampm(ampm)
        self.actions.select_entry_date(date, type_in)

    def choose_exit_time_date(self, time, ampm, date, type_in):
        self.actions.select_exit_time(time)
        self.actions.select_exit_ampm(ampm)
        self.actions.select_exit_date(date, type_in)

    def calculate(self):
        self.actions.calculate()

    def price(self):
        self.actions.price()


class PickDate(BasePage):

    def select_month(self, month):
        self.actions.select_month(month)

    def select_year(self, year):
        self.actions.select_year(year)

    def select_day(self, day):
        self.actions.select_day(day)