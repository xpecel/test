from django.apps import AppConfig


class GenericConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "generic"

class AppNameConfig(AppConfig):
    name = 'generic'
    def ready(self):
        from scheduler import scheduler
        scheduler.start()
