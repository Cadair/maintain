from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Car, Fuel, MileageLog, Part, Reminder, Service, User


class CarAdmin(admin.ModelAdmin):
    list_display = ["owner", "id", "make", "model", "default"]


class LogAdmin(admin.ModelAdmin):
    list_display = ["timestamp", "car", "mileage"]


# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(MileageLog, LogAdmin)
admin.site.register(Fuel)
admin.site.register(Service)
admin.site.register(Part)
admin.site.register(Reminder)
