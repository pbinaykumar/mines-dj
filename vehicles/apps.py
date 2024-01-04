from django.apps import AppConfig

class VehiclesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vehicles'

    def ready(self):
        pass
            # Start the Firebase listener when the Django application starts
            # import vehicles.firebase_listener