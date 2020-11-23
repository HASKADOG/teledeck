# -*- coding: utf-8 -*-
from yandex_checkout.domain.common.payment_method_type import PaymentMethodType
from yandex_checkout.domain.models.payment_data.payment_data import ResponsePaymentData


class PaymentDataGooglePay(ResponsePaymentData):

    def __init__(self, *args, **kwargs):
        super(PaymentDataGooglePay, self).__init__(*args, **kwargs)
        if self.type is None or self.type is not PaymentMethodType.GOOGLE_PAY:
            self.type = PaymentMethodType.GOOGLE_PAY
