from django.db import models

# Create your models here.

class mileage_user(models.Model):
    username =  models.CharField(max_length=20, unique=True, null=False)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.id} | Username: {self.username} | Email: {self.email}"

    @property
    def last_date(self):
        return self.user_entry.latest('date_entered').date_entered


class mileage_entry(models.Model):
    date_entered = models.DateField(null=False)
    locations = models.CharField(max_length=120, null=False)
    miles_driven = models.FloatField(null=False)
    mileage_user_key = models.ForeignKey(mileage_user, on_delete=models.CASCADE, related_name="user_entry")

    def __str__(self):
        return f"{self.mileage_user_key} - Username: Date entered: {self.date_entered} Miles Driven: {self.miles_driven} Locations: {self.locations}"

class Trip(models.Model):
    location_1 = models.CharField(max_length=36, null=False)
    location_2 = models.CharField(max_length=36, null=False)
    miles_driven = models.FloatField(null=False)
    date_driven = models.DateField(null=False)
    mileage_user_key = models.ForeignKey(mileage_user, on_delete=models.CASCADE, related_name="userID_trip")

    def __str__(self):
        return f"User ID: {self.mileage_user_key} | Date entered: {self.date_driven} | Miles Driven: {self.miles_driven} | Start Location: {self.location_1} | End Location: {self.location_2}"
