from django.db import models


# Create your models here.

class Fuel(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class PostcodesGeo(models.Model):
    id = models.AutoField(primary_key=True)
    postcode = models.CharField(max_length=5, blank=True, null=True)
    suburb = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=4, blank=True, null=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=5, blank=True,
                                   null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    longitude = models.DecimalField(max_digits=10, decimal_places=5, blank=True,
                                    null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        managed = False
        db_table = 'postcodes_geo'
