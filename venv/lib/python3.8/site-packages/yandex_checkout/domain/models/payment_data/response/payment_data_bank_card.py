# -*- coding: utf-8 -*-
from yandex_checkout.domain.common.payment_method_type import PaymentMethodType
from yandex_checkout.domain.models.payment_data.payment_data import ResponsePaymentData
from yandex_checkout.domain.models.payment_data.response.credit_card import CreditCard


class PaymentDataBankCard(ResponsePaymentData):
    __card = None

    def __init__(self, *args, **kwargs):
        super(PaymentDataBankCard, self).__init__(*args, **kwargs)
        if self.type is None or self.type is not PaymentMethodType.BANK_CARD:
            self.type = PaymentMethodType.BANK_CARD

    @property
    def card(self):
        return self.__card

    @card.setter
    def card(self, value):
        if isinstance(value, dict):
            self.__card = CreditCard(value)
        elif isinstance(value, CreditCard):
            self.__card = value
        else:
            raise TypeError('Invalid card value type in PaymentDataBankCard')

