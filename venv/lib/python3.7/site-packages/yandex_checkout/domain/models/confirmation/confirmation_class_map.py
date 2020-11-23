# -*- coding: utf-8 -*-
from yandex_checkout.domain.common.confirmation_type import ConfirmationType
from yandex_checkout.domain.common.data_context import DataContext
from yandex_checkout.domain.models.confirmation.request.confirmation_embedded import \
    ConfirmationEmbedded as RequestConfirmationEmbedded
from yandex_checkout.domain.models.confirmation.request.confirmation_external import \
    ConfirmationExternal as RequestConfirmationExternal
from yandex_checkout.domain.models.confirmation.request.confirmation_qr import \
    ConfirmationQr as RequestConfirmationQr
from yandex_checkout.domain.models.confirmation.request.confirmation_redirect import \
    ConfirmationRedirect as RequestConfirmationRedirect
from yandex_checkout.domain.models.confirmation.response.confirmation_embedded import \
    ConfirmationEmbedded as ResponseConfirmationEmbedded
from yandex_checkout.domain.models.confirmation.response.confirmation_external import \
    ConfirmationExternal as ResponseConfirmationExternal
from yandex_checkout.domain.models.confirmation.response.confirmation_qr import \
    ConfirmationQr as ResponseConfirmationQr
from yandex_checkout.domain.models.confirmation.response.confirmation_redirect import \
    ConfirmationRedirect as ResponseConfirmationRedirect


class ConfirmationClassMap(DataContext):
    def __init__(self):
        super(ConfirmationClassMap, self).__init__(('request', 'response'))

    @property
    def request(self):
        return {
            ConfirmationType.REDIRECT: RequestConfirmationRedirect,
            ConfirmationType.EXTERNAL: RequestConfirmationExternal,
            ConfirmationType.EMBEDDED: RequestConfirmationEmbedded,
            ConfirmationType.QR: RequestConfirmationQr
        }

    @property
    def response(self):
        return {
            ConfirmationType.REDIRECT: ResponseConfirmationRedirect,
            ConfirmationType.EXTERNAL: ResponseConfirmationExternal,
            ConfirmationType.EMBEDDED: ResponseConfirmationEmbedded,
            ConfirmationType.QR: ResponseConfirmationQr
        }
