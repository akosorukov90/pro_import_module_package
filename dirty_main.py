import datetime
from application.salary import *
from application.db.people import *

if __name__ == '__main__':
    print(f'Текущая дата: {datetime.datetime.now()}')
    calculate_salary()
    get_employees()
