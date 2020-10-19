# -*- coding: utf-8 -*-
from yandex_checkout.domain.common.confirmation_type import ConfirmationType
from yandex_checkout.domain.models.confirmation.request.confirmation_request import ConfirmationRequest


class ConfirmationQr(ConfirmationRequest):
    """
    Class representing qr confirmation data object
    """

    def __init__(self, *args, **kwargs):
        super(ConfirmationQr, self).__init__(*args, **kwargs)
        if self.type is None or self.type is not ConfirmationType.QR:
            self.type = ConfirmationType.QR
