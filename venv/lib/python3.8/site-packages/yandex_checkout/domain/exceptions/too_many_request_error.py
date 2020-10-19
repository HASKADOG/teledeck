# -*- coding: utf-8 -*-
from yandex_checkout.domain.exceptions.api_error import ApiError


class TooManyRequestsError(ApiError):
    HTTP_CODE = 429
