from django.apps import AppConfig


class SklepConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sklep'

    def ready(self):
        from . import signals
