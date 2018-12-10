from django.contrib import admin

from .models import mileage_user, mileage_entry, NickTrip, Trip

# Register your models here.

admin.site.register(mileage_user)
admin.site.register(mileage_entry)
admin.site.register(NickTrip)
admin.site.register(Trip)
