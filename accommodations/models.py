from django.db import models

class Accommodation(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability_start = models.DateField()
    availability_end = models.DateField()
    number_of_beds = models.IntegerField()
    distance_to_hku = models.FloatField()

    def __str__(self):
        return self.name