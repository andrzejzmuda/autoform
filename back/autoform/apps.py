from django.apps import AppConfig


class AutoformConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'autoform'

    def ready(self):
        from . import signals
        print('ready')
