from app import db
from app.models import Time
import datetime

for i in range(1, 32):
    a = Time(date=datetime.datetime.strptime('{}.2.2021'.format(i), '%d.%m.%Y'), taken=False)
    db.session.add(a)
    db.session.commit()
