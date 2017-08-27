from selenium.webdriver.common.by import By


class CalcPageLocators(object):
    Lot = (By.NAME, 'Lot')
    Options = (By.TAG_NAME, 'option')
    EntryTime = (By.ID, 'EntryTime')
    EntryDate = (By.ID, 'EntryDate')
    ExitTime = (By.ID, 'ExitTime')
    ExitDate = (By.ID, 'ExitDate')
    EntryAMPM = (By.NAME, 'EntryTimeAMPM')
    ExitAMPM = (By.NAME, 'ExitTimeAMPM')
    DatePicker = (By.TAG_NAME, 'img')
    Calculate = (By.NAME, 'Submit')
    Cost = (By.TAG_NAME, 'b')
    Duration = (By.TAG_NAME, 'b')
    Error = (By.TAG_NAME, 'b')


class PickDateLocators(object):
    Month = (By.NAME, 'MonthSelector')
    Year = (By.TAG_NAME, 'b')
    #Day = (By.LINK_TEXT, '26')

