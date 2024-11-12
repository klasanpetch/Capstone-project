from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(999999)])
    bookingDate = models.DateField()
    
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(99999)])

    