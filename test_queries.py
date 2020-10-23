from app import db
from app.models import Users, Ads, Variables
import datetime
import requests

params = {
    "SECRET_KEY":'1488',
    "METHOD":'update_status'
}

data = {
    'TRACK_CODE':'d6945c',
    'STATUS':4,
    'COMMENT':"теацфвст тест",
    'AUTHOR':'тесттест'
}



result = requests.post(url='http://127.0.0.1:5000/api', params = params, data=data)

print(result)
print(result.text)

a = 1