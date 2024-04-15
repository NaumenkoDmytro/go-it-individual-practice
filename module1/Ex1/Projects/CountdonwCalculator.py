# #Write some code that can take two dates as input, 
# and then calculate the amount of time between them. 
# This will be a great way to familiarize yourself with Python’s datetime module.

from datetime import datetime

#user input in STR format
start_date = input('Please, enter the start date in format (2020.01.01):')
end_date = input('Please, enter the end date (2020.01.01):')

#Function that calculated the differnce with datetime objects
def calcualting_amount_betwen_dates(start_period: str, end_period: str):
    formated_start_date = datetime.strptime(start_period, "%Y.%m.%d").date()
    formated_end_date = datetime.strptime(end_period, "%Y.%m.%d").date()

    dif_counter = formated_end_date - formated_start_date
    return dif_counter

def string_output(time_dif: datetime):
    print(time_dif)
    time_dif_str = int(time_dif)
    x = time_dif_str
    print(type(x))
    return x



print(string_output(calcualting_amount_betwen_dates(start_date, end_date)))

