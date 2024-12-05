from django.db import models

class Booking(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    room_type = models.CharField(max_length=50)
    move_in_date = models.DateField()

    def __str__(self):
        return f"{self.full_name} - {self.room_type}"



