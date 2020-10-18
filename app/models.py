from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


#
# This file defines the database architecture.
#

@login.user_loader
def load_user(id):
    return Users.query.get(int(id))


# Users table.
class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    second_name = db.Column(db.String(64))
    third_name = db.Column(db.String(64))
    is_entity = db.Column(db.Boolean)
    entity_name = db.Column(db.String(64))
    iin = db.Column(db.Integer)
    ogrn = db.Column(db.Integer)
    email = db.Column(db.String(128), unique=True)
    password_hash = db.Column(db.String(128))
    phone_number = db.Column(db.BigInteger)
    status = db.Column(db.String(8))
    ref_code = db.Column(db.String(16), unique=True)
    ref_master_code = db.Column(db.String(16))
    register_date = db.Column(db.DateTime)
    collected_m = db.Column(db.Integer)
    ads = db.relationship('Ads', backref='user', lazy='dynamic')
    ref_master = db.Column(db.Integer)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User username={}>'.format(self.username)


# Ads table.
class Ads(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    track = db.Column(db.String(64), unique=True)
    notify_email = db.Column(db.String(128))
    is_entity = db.Column(db.Boolean)
    entity_name = db.Column(db.String(64))
    iin = db.Column(db.Integer)
    ogrn = db.Column(db.Integer)
    username = db.Column(db.String(64))
    second_name = db.Column(db.String(64))
    third_name = db.Column(db.String(64))
    individual_phone_number = db.Column(db.BigInteger)
    promocode = db.Column(db.String(16))
    duration = db.Column(db.Integer)
    ad_type = db.Column(db.String(20))
    is_custom = db.Column(db.Boolean)
    template_data = db.Column(db.String(512))
    img_path = db.Column(db.String(256))
    status = db.Column(db.Integer)
    comment = db.Column(db.String(64))
    author = db.Column(db.String(64))
    apply_date = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    masters_money = db.Column(db.Integer)
    new = db.Column(db.Boolean)
    edited = db.Column(db.Boolean)
    paid = db.Column(db.Boolean)
    price = db.Column(db.Integer)
    debug = db.Column(db.String(22))
    time = db.Column(db.String(512))
    ref_discount = db.Column(db.Integer)
    updates = db.relationship('Ads_updates', backref='ad', lazy='dynamic')

    def __repr__(self):
        return '<Ad id={}>'.format(self.id)


# Variables table
class Variables(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    value = db.Column(db.Integer)

    def __repr__(self):
        return '<Variable name={} value={}>'.format(self.name, self.value)


# Ads updates table
class Ads_updates(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ad_id = db.Column(db.Integer, db.ForeignKey('ads.id'))
    status = db.Column(db.Integer)
    comment = db.Column(db.String(64))
    author = db.Column(db.String(64))

    def __repr__(self):
        return '<Update id={}>'.format(self.id)


# Available time table
class Time(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    taken = db.Column(db.Boolean)


# Promocodes
class Promocodes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    promocode = db.Column(db.String(32))
    date_start = db.Column(db.Date)
    date_expires = db.Column(db.Date)
    discount = db.Column(db.Integer)
