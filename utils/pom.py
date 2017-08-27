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

    def ChooseLot(self, lot):
        self.actions.select_lot(lot)

    def ChooseEntryTimeDate(self, time, ampm, date, type_in):
        self.actions.select_entry_time(time)
        self.actions.select_entry_ampm(ampm)
        self.actions.select_entry_date(date, type_in)

    def ChooseExitTimeDate(self, time, ampm, date, type_in):
        self.actions.select_exit_time(time)
        self.actions.select_exit_ampm(ampm)
        self.actions.select_exit_date(date, type_in)

    def Calculate(self):
        self.actions.calculate()

    def Price(self):
        self.actions.price()


class PickDate(BasePage):

    def SelectMonth(self, month):
        self.actions.select_month(month)

    def SelectYear(self, year):
        self.actions.select_year(year)

    def SelectDay(self, day):
        self.actions.select_day(day)