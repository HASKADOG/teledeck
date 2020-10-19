import uuid

from yandex_checkout import Configuration, Payment

Configuration.account_id = '501490'
Configuration.secret_key = 'test_aDEqLUxN9tfEWmK3vRb5R2b8x6PULdS_62Y6o77B_8w'

payment = Payment.create({
    "amount": {
        "value": "1.00",
        "currency": "RUB"
    },
    "confirmation": {
        "type": "redirect",
        "return_url": "https://vk.com/id608742663"
    },
    "capture": True,
    "description": "Заказ №1"
}, uuid.uuid4())

a = 1