from django_payment_gateways.modules.abstracts import Driver
from django_payment_gateways.modules.drivers.zarinpal.strategies.sandbox import Sandbox
from django_payment_gateways.modules.invoice import Invoice


class Zarinpal(Driver):
    strategies = {
        'sandbox': Sandbox
    }

    def __init__(self, invoice: Invoice, settings: dict):
        self.invoice = invoice
        self.settings = settings
        self.strategy = self._get_fresh_strategy_instance(invoice, settings)

    def purchase(self):
        return self.strategy.purchase()

    def pay(self):
        return self.strategy.pay()

    def verify(self, request):
        return self.strategy.verify(request)

    def _get_fresh_strategy_instance(self, invoice: Invoice, settings: dict):
        strategy = self.strategies[self._get_mode()]
        return strategy(invoice, settings)

    def _get_mode(self):
        return str(self.settings.get('mode')).lower()
