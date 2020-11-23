# -*- coding: utf-8 -*-

from yandex_checkout.domain.common.base_object import BaseObject
from yandex_checkout.domain.common.data_context import DataContext


class RequestObject(BaseObject):
    """
    Base class for request objects
    """
    @staticmethod
    def context():
        return DataContext.REQUEST

    def validate(self):
        """
        Validate request data
        """
        pass
