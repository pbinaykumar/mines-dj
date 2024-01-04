from django.core.management.base import BaseCommand
from firebase_admin import db
import firebase_admin
from firebase_admin import credentials
from .models import VehicleStatus, Vehicle

# Replace 'path/to/your/firebase-credentials.json' with the actual path to your JSON credentials file.
cred = credentials.Certificate("F:\\CodeWorld\\X\\PyPython\\DJ\\mines\\mines-1de83-firebase-adminsdk-pckww-e3ee4b4ba1.json")
firebase_admin.initialize_app(cred, {'databaseURL':'https://mines-1de83-default-rtdb.firebaseio.com'})
# Reference to the Firebase Realtime Database
ref = db.reference('/new_plant')

import signal
import sys

def signal_handler(sig, frame):
    # Handle the SIGINT signal (e.g., stop the Firebase listener and exit)
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def handle_event(event):
    # Handle the event data
    data = ref.get()
    for key,value in data.items():
        try:
            vehicle = Vehicle.objects.get(vehicle_tag_id=key)
            try:
                vehicle_status = VehicleStatus.objects.get(vehicle=vehicle,active=True)
                if vehicle_status.status == value:
                    pass
                elif (vehicle_status.status == '1' or vehicle_status.status == '2') and (value == '3' or value == '4'):
                    vehicle_status.status = value
                    vehicle_status.save()
                elif vehicle_status.status == '3' and value== '4':
                    vehicle_status.status = value
                    vehicle_status.save()
                elif vehicle_status.status == '4' and value == '5':
                    vehicle_status.status = value
                    vehicle_status.active = False
                    vehicle_status.save()

            except Exception as e:
                if value == '1' or value == '2':
                    VehicleStatus(vehicle=vehicle, status=value).save()
        except Exception as e:
            pass




# Listen to changes in the Firebase Realtime Database
ref.listen(handle_event)

