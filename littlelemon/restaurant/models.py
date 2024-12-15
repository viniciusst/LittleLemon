from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    noOfGuests = models.IntegerField()
    bookingDate = models.DateTimeField(db_index=True)

    def __str__(self) -> str:
        return self.name

class Menu(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)
    inventory = models.IntegerField()

    def __str__(self) -> str:
        return self.title
