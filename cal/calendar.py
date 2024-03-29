import datetime
from sqlalchemy import extract
from app import db
from app.models import Time, Promocodes


class Calendar():

    def __init__(self, today=datetime.datetime.now()):
        self.today = today
        year = self.today.year
        leap_years = [2020, 2024, 2028, 2032, 2036]

        if year in leap_years:
            jan_d = 29
        else:
            jan_d = 28

        self.months = [
            {'name': 'Январь', 'days_qty': 31},
            {'name': 'Февраль', 'days_qty': jan_d},
            {'name': 'Март', 'days_qty': 31},
            {'name': 'Апрель', 'days_qty': 30},
            {'name': 'Май', 'days_qty': 31},
            {'name': 'Июнь', 'days_qty': 30},
            {'name': 'Июль', 'days_qty': 31},
            {'name': 'Август', 'days_qty': 31},
            {'name': 'Сентябрь', 'days_qty': 30},
            {'name': 'Октябрь', 'days_qty': 31},
            {'name': 'Ноябрь', 'days_qty': 30},
            {'name': 'Декабрь', 'days_qty': 31}
        ]

    def get_calendar(self, month_n, year, promo=None):

        print(self.today)

        if promo:
            promed = True
        else:
            promed = False

        if month_n == 0:
            year_q = year - 1
            month_n = 12
        else:
            year_q = year

        month_n = int(month_n) - 1
        now = self.today
        out = {
            'month': self.months[0 if month_n == 12 else month_n]['name'],
            'month_n': month_n + 1,
            'year': year_q,
            'start': self.today,
            'days': []
        }
        sale = 0
        try:

            print('|{}|{}'.format(month_n+1, year_q))
            month_db = Time.query.filter(extract('month', Time.date) == (1 if month_n + 1 == 13 else month_n + 1), extract('year', Time.date) == (year_q))

            # holidays check
            date_to_skip = 0
            for date in month_db:
                if date.date == now.date():
                    if month_db[date.date.day].taken == 1 and now.hour >= 13:
                        holidays = 0
                        iterator = date.date.day
                        while month_db[iterator + 1].taken == 1:
                            holidays += 1
                            iterator += 1
                        date_to_skip = month_db[iterator + 1].date
                        print('skipping {}'.format(date_to_skip))
            for date in month_db:
                if promo:
                    promo_data = Promocodes.query.filter_by(promocode=promo).first()
                    if promo_data:
                        sale = 1 if promo_data.date_start <= date.date and promo_data.date_expires >= date.date else 0



                out['days'].append(
                    {
                        'number': date.date.day,
                        'available': 0 if ((now.hour >= 13) and (
                                now.month == date.date.month and now.year == date.date.year and date.date.day - now.day == 1) or (
                                                   now.date() >= date.date) or (date.taken == True) or (date.date == date_to_skip) or (promed and sale == 0)) else 1,
                        'sale': sale,
                        'date': date.date.strftime('%d.%m.%Y'),
                        'next_m': 0,
                        'promed': promo if promed else 0
                    }
                )
                sale = 0
        except IndexError:
            for i in range(self.months[0 if month_n == 12 else month_n]['days_qty']):
                out['days'].append(
                    {
                        'number': i + 1,
                        'available': 0,
                        'sale': 0,
                        'date': 'Нет в расписании!',
                        'next_m': 0,
                        'promed': 0
                    }
                )
                sale = 0

        try:
            print('next_m {}'.format(1 if month_n + 2 == 13 else month_n + 2))
            month_next = Time.query.filter(extract('month', Time.date) == (1 if month_n + 2 == 13 else month_n + 2), extract('year', Time.date) == (year_q))

            for i in range(0, 36 - self.months[0 if month_n == 12 else month_n]['days_qty']):
                out['days'].append(
                    {
                        'number': '{} >'.format(month_next[i].date.day),
                        'available': 0,
                        'sale': sale,
                        'date': month_next[i].date.strftime('%d.%m.%Y'),
                        'next_m': 1,
                        'promed': 0
                    }
                )

                sale = 0
        except IndexError:
            for i in range(0, 36 - self.months[0 if month_n == 12 else month_n]['days_qty']):
                out['days'].append(
                    {
                        'number': 'X',
                        'available': 0,
                        'sale': 0,
                        'date': 'Нет в расписании!',
                        'next_m': 0,
                        'promed': 0
                    }
                )
                sale = 0
        return out
