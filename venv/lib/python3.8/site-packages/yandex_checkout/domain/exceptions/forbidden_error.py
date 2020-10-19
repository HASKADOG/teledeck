# -*- coding: utf-8 -*-
from yandex_checkout.domain.exceptions.api_error import ApiError


class ForbiddenError(ApiError):
    HTTP_CODE = 403

