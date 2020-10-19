# -*- coding: utf-8 -*-
from yandex_checkout.domain.common.base_object import BaseObject
from yandex_checkout.domain.models.amount import Amount


class Transfer(BaseObject):
    """
    Class representing payment transfer wrapper object

    Used in Payment
    """
    __account_id = None

    __amount = None

    @property
    def account_id(self):
        return self.__account_id

    @account_id.setter
    def account_id(self, value):
        self.__account_id = str(value)

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        if isinstance(value, dict):
            self.__amount = Amount(value)
        elif isinstance(value, Amount):
            self.__amount = value
        else:
            raise TypeError('Invalid transfer.amount value type')
