# -*- coding: utf-8 -*-
from yandex_checkout.domain.common.type_factory import TypeFactory
from yandex_checkout.domain.models.payment_data.payment_data_class_map import PaymentDataClassMap


class PaymentDataFactory(TypeFactory):
    """
    Factory for payment data objects
    """

    def __init__(self):
        super(PaymentDataFactory, self).__init__(PaymentDataClassMap())
