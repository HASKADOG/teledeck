# -*- coding: utf-8 -*-
from yandex_checkout import PaymentResponse
from yandex_checkout.domain.common.response_object import ResponseObject


class PaymentListResponse(ResponseObject):
    __type = None

    __next_page = None

    __items = None

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value

    @property
    def next_page(self):
        return self.__next_page

    @next_page.setter
    def next_page(self, value):
        self.__next_page = value

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, value):
        if isinstance(value, list):
            self.__items = [PaymentResponse(payment) for payment in value]
        else:
            self.__items = value
