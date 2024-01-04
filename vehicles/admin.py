from django.contrib import admin
from .models import Vehicle, VehicleStatus
# Register your models here.

class VehicleAdmin(admin.ModelAdmin):
    list_display = ["vehicle_tag_id","vehicle_number","vehicle_name","created_at","modified_at"]
admin.site.register(Vehicle,VehicleAdmin)

class VehicleStatusAdmin(admin.ModelAdmin):
    list_display = ["vehicle","status","active","created_at","modified_at"]
admin.site.register(VehicleStatus,VehicleStatusAdmin)
