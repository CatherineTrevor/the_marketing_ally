from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = 'contact'

    def ready(self):
        import contact.signals
