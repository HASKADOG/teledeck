import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '79f09018cae1fe315233f8447ad1bbdd'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://efir:TeledeckEfir24@efir.ru@91.210.171.60:3306/alchemy'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TEMPLATES_AUTO_RELOAD = True
