from django.contrib import admin
from .models import Car, User, Equipment, Mileage_History, Report

admin.site.register(Car)
admin.site.register(User)
admin.site.register(Equipment)
admin.site.register(Mileage_History)
admin.site.register(Report)