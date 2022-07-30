from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Seat(models.Model):
    number = models.CharField(max_length=15)
    first_class = models.BooleanField(default=False)

class Airplane(models.Model):
    model = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

class Ticket(models.Model):
    date = models.DateField()
    hour = models.CharField(max_length=15)
    origin = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE, related_name="seats")
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE, related_name="airplanes")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets')
