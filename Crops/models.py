from django.db import models

# Create your models here.


class Wheat(models.Model):
    # Date_of_harvest = models.DateField()
    # Section = models.IntegerField()
    Uid = models.TextField()
    # Food_Type = models.TextField(max_length=255, null=True)
    Temp = models.FloatField(null=True)
    Humidity = models.FloatField(null=True)
    Weight = models.FloatField(null=True)
    CO2 = models.FloatField(null=True)
    O2 = models.FloatField(null=True)
    Ethylene = models.FloatField(null=True)
    Light_Value = models.FloatField(null=True)

    # Price = models.FloatField(null=True, blank=True)
    # Est_date_of_exp = models.DateField()
