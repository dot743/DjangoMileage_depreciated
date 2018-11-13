from django.db import models

# Create your models here.

class mileage_user(models.Model):
    username =  models.CharField(max_length=20, unique=True, null=False)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.id} - Username: {self.username} Email: {self.email}"

class mileage_entry(models.Model):
    date_entered = models.DateField(null=False)
    locations = models.CharField(max_length=120, null=False)
    miles_driven = models.FloatField(null=False)
    mileage_user_key = models.ForeignKey(mileage_user, on_delete=models.CASCADE, related_name="user_entry")

    def __str__(self):
        return f"Username: {self.mileage_user} Date entered: {self.date_entered} Miles Driven: {self.miles_driven} Locations: {self.locations}"
