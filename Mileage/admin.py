from django.contrib import admin

from .models import mileage_user, mileage_entry, Trip

# Register your models here.

admin.site.register(mileage_user)
admin.site.register(mileage_entry)
admin.site.register(Trip)
