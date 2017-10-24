#   Parking calculator - test exercise.

Basic test automation for parking calculator http://adam.goucher.ca/parkcalc using Selenium WebDriver, Python, Pytest.
PageObject model has been used to implement facade methods.
PyTest has been used to organize tests, i.e. generic test case with parameters has been created using @pytest.mark.parametrize() fixture

## Test cases:

>    #### @pytest.mark.parametrize('lot, entryTimeDate, exitTimeDate, result',
>                   [('EP', ('03:00', 'PM', '08/25/2017', False),           # 1.Valid entry/exit
>                           ('04:00', 'PM', '08/25/2017', False), '$ 4.00'),#   time/dates. Dates are selected via popup
>                    ('EP', ('03:00', 'PM', '08/30/2017', True),            # 2.Entry date after
>                           ('06:00', 'PM', '08/29/2017', False), ERROR),   #   exit date. Exit date is selected via popup
>                    ('STP', ('03:00', 'PM', '09/02/2017', True),           # 3.Entry date after
>                            ('06:00', 'PM', '09/01/2017', True), ERROR),   #   exit date. Dates are typed in
>                    ('LTS', ('02:00', 'PM', '08/30/2017', False),          # 4.Entry time after
>                            ('01:00', 'PM', '08/29/2017', True), ERROR),   #   exit time.
>                    ('EP',  ('01:00', 'AM', '123/132/231', True),          # 5.Invalid date format
>                            ('03:00', 'AM', '88/291/2167', True), ERROR),  #   Dates are typed in
>                    ('LTG', ('AA:xx', 'AM', '08/28/2017', True),           # 6.Invalid time format
>                            ('BB:yy', 'AM', '08/29/2017', True), ERROR),   #   Time is typed in
>                    ('VP',  ('01:00', 'AM', 'MM/DD/YYYY', True),           # 7.Invalid date format
>                            ('02:00', 'AM', 'MM/DD/YYYY', True), FORMAT_ERROR) # Date is typed in
>                   ]
> ####                       )

### 1.Valid entry/exit time/dates. Dates are selected via popup
 > a. Select lot 'Economy Parking' ('EP')
  b. Select entry time/date via popup ('03:00', 'PM', '08/25/2017', False). False means the date is to be selected via popup  (True = type in)
  c. Select exit time/date via popup ('04:00', 'PM', '08/25/2017', False)
  d. Expected result = $ 4.00 

### 2.Entry date is after exit date. Exit date is selected via popup
>  a. Select lot 'Economy Parking' ('EP')
   b.Select entry time/date via popup ('03:00', 'PM', '08/30/2017', True). 
  c. Select exit time/date via popup ('06:00', 'PM', '08/29/2017', False)
  d. Expected result = ERROR ('ERROR! YOUR EXIT DATE OR TIME IS BEFORE YOUR ENTRY DATE OR TIME')

.
.
.

### 7.Invalid date format. Date is typed in.
>  a. Select lot 'Valet Parking' ('VP')
  b. b.Select entry time/date via popup ('01:00', 'AM', 'MM/DD/YYYY', True). 
  c.Select exit time/date via popup ('02:00', 'AM', 'MM/DD/YYYY', False)
  d. Expected result = FORMAT_ERROR (''ERROR! ENTER A CORRECTLY FORMATTED DATE'')
  
### Bugs:

1. Entry date after exit date is processed incorrectly, i.e. 
    AssertionError: assert '$ 12.00' ==  ERROR! YOUR EXIT DATE OR TIME IS BEFORE YOUR ENTRY DATE OR TIME
   See test case 2 for steps to reproduce.

2. Entry time after exit time is processed incorrectly, i.e.
    AssertionError: assert '$ 0.00' == ERROR! YOUR EXIT DATE OR TIME IS BEFORE YOUR ENTRY DATE OR TIME
   See test case 4 for steps to reproduce.

3. Invalid date format is processed incorrectly, i.e.
    AssertionError: assert '$ 5,447,870.00' == ERROR! YOUR EXIT DATE OR TIME IS BEFORE YOUR ENTRY DATE OR TIME

p.s. There are many more bugs. The above is just to describe the concept of Selenium WebDriver + Pytest testing.

References:
https://github.com/hhatcher/parkcalctest
https://github.com/gunesmes/page-object-python-selenium
https://justin.abrah.ms/python/selenium-page-object-pattern--the-key-to-maintainable-tests.html
http://selenium-python.readthedocs.io/  
