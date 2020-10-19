# -*- coding: utf-8 -*-
from yandex_checkout.domain.common.base_object import BaseObject
from yandex_checkout.domain.models.amount import Amount


class TransferResponse(BaseObject):
    """
    Class representing payment transfer wrapper object

    Used in Payment
    """
    __account_id = None

    __amount = None

    __status = None

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
            raise TypeError('Invalid amount value type')

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = str(value)


class TransferStatus(object):
    """
    Class representing transfer.status values enum
    """
    PENDING = 'pending'
    WAITING_FOR_CAPTURE = 'waiting_for_capture'
    SUCCEEDED = 'succeeded'
    CANCELED = 'canceled'
