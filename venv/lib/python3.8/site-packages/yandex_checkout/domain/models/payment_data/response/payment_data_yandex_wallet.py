# -*- coding: utf-8 -*-
from yandex_checkout.domain.common.payment_method_type import PaymentMethodType
from yandex_checkout.domain.models.payment_data.payment_data import ResponsePaymentData


class PaymentDataYandexWallet(ResponsePaymentData):
    def __init__(self, *args, **kwargs):
        super(PaymentDataYandexWallet, self).__init__(*args, **kwargs)
        if self.type is None or self.type is not PaymentMethodType.YANDEX_MONEY:
            self.type = PaymentMethodType.YANDEX_MONEY
