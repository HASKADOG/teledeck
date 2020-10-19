# -*- coding: utf-8 -*-
from deprecated import deprecated
from yandex_checkout.domain.common.payment_method_type import PaymentMethodType
from yandex_checkout.domain.models.payment_data.payment_data import ResponsePaymentData


@deprecated("This class will be removed in one of future versions")
class PaymentDataWechat(ResponsePaymentData):
    def __init__(self, *args, **kwargs):
        super(PaymentDataWechat, self).__init__(*args, **kwargs)
        if self.type is None or self.type is not PaymentMethodType.WECHAT:
            self.type = PaymentMethodType.WECHAT
