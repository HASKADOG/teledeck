# -*- coding: utf-8 -*-


class ConfirmationType:
    """
    Constants representing confirmation types. Available values are:

    * yandex_checkout.domain.common.ConfirmationType.EXTERNAL
    * yandex_checkout.domain.common.ConfirmationType.REDIRECT
    * yandex_checkout.domain.common.ConfirmationType.EMBEDDED
    * yandex_checkout.domain.common.ConfirmationType.QR
    """
    EMBEDDED = 'embedded'
    EXTERNAL = 'external'
    REDIRECT = 'redirect'
    QR = 'qr'
