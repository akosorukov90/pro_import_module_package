import datetime
from application.salary import *
from application.db.people import *

if __name__ == '__main__':
    now = datetime.datetime.now()
    print(f'Текущая дата: {now.strftime("%d.%m.%Y")}')
    calculate_salary()
    get_employees()
