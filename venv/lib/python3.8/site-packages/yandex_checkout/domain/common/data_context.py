# -*- coding: utf-8 -*-
from yandex_checkout.domain.common.context import Context


class DataContext(Context):
    """
    Constants representing context data types. Available values are:

    * yandex_checkout.domain.common.DataContext.REQUEST
    * yandex_checkout.domain.common.DataContext.RESPONSE
    """
    REQUEST = 'request'
    RESPONSE = 'response'
