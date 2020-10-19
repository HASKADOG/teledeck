# -*- coding: utf-8 -*-
from yandex_checkout.domain.common.base_object import BaseObject


class Confirmation(BaseObject):
    """
    Base class confirmation data objects
    """
    __type = None

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = str(value)
