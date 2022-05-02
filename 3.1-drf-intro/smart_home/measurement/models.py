from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=511, null=True, blank=True)


class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor, related_name="measurements",
                                  on_delete=models.CASCADE)
    measured_temperature = models.FloatField()
    measurement_date = models.DateField(auto_now_add=True)
    image = models.ImageField(max_length=255, null=True, blank=True)
