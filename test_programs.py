from app import db
from app.models import Time
import datetime

for i in range(1, 32):
    date = datetime.datetime.strptime('{}.11.2020'.format(i), '%d.%m.%Y')
    if date.weekday() == 5 or date.weekday() == 6:
        a = Time(date = date, taken=True)
    else:
        a = Time(date = date, taken=False)
    db.session.add(a)
    db.session.commit()
