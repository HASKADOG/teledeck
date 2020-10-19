# -*- coding: utf-8 -*-
from yandex_checkout.domain.common.type_factory import TypeFactory
from yandex_checkout.domain.models.confirmation.confirmation_class_map import ConfirmationClassMap


class ConfirmationFactory(TypeFactory):
    def __init__(self):
        super(ConfirmationFactory, self).__init__(ConfirmationClassMap())
