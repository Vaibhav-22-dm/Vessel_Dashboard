from django.db import models

# Create your models here.
class Port(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    lat = models.CharField(max_length=255, null=True, blank=True)
    long = models.CharField(max_length=255, null=True, blank=True)
    dock_system = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.name)
    
class Vessel(models.Model):
    mmsi = models.CharField(max_length=255, unique=True, null=True, blank=True)
    port = models.ForeignKey(Port, null=True, blank=True, on_delete=models.CASCADE)
    length = models.IntegerField(null=True, blank=True)
    breadth = models.IntegerField(null=True, blank=True)
    nationality = models.CharField(max_length=255, null=True, blank=True)
    draft = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True)
    dwt = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.mmsi)

