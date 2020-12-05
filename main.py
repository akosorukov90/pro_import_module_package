import datetime
from application.salary import calculate_salary
from application.db.people import get_employees


if __name__ == '__main__':
    now = datetime.datetime.now()
    print(f'Текущая дата: {now.strftime("%d.%m.%Y")}')
    calculate_salary()
    get_employees()
