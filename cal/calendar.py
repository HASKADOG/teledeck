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
        month_n = int(month_n) - 1
        now = self.today
        print(month_n)
        out = {
            'month': self.months[0 if month_n == 12 else month_n]['name'],
            'month_n': month_n + 1,
            'year': year,
            'days': []
        }
        sale = 0
        try:
            print('current_m {}'.format(1 if month_n + 1 == 13 else month_n + 1))

            if month_n == 0:
                year_q = year - 1
                month_n = 12
            else:
                year_q = year

            month_db = Time.query.filter(extract('month', Time.date) == (1 if month_n + 1 == 13 else month_n + 1), extract('year', Time.date) == (year_q))

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
                                                   now.date() >= date.date) or (date.taken == True)) else 1,
                        'sale': sale,
                        'date': date.date.strftime('%d.%m.%Y')
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
                        'date': 'Нет в расписании!'
                    }
                )
                sale = 0

        try:
            print('next_m {}'.format(1 if month_n + 2 == 13 else month_n + 2))
            month_next = Time.query.filter(extract('month', Time.date) == (1 if month_n + 2 == 13 else month_n + 2), extract('year', Time.date) == (year))

            for i in range(0, 36 - self.months[0 if month_n == 12 else month_n]['days_qty']):
                out['days'].append(
                    {
                        'number': month_next[i].date.day,
                        'available': 0 if ((now.hour >= 13 and now.month > month_next[i].date.month and now.year ==
                                            month_next[i].date.year and month_next[i].date.day - now.day == 1) or (
                                                       now.date() >= month_next[i].date) or (
                                                       month_next[i].taken == True)) else 1,
                        'sale': sale,
                        'date': month_next[i].date.strftime('%d.%m.%Y')
                    }
                )

                sale = 0
        except IndexError:
            for i in range(0, 36 - self.months[0 if month_n == 12 else month_n]['days_qty']):
                out['days'].append(
                    {
                        'number': i + 1,
                        'available': 0,
                        'sale': 0,
                        'date': 'Нет в расписании!'
                    }
                )
                sale = 0
        return out
