from django.db import models
from django.contrib.auth.models import User
from Ports.models import *

# Create your models here.
class Employee(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    port = models.ForeignKey(Port, null=True, blank=True, on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=255, null=True, blank=True)
    device_id = models.CharField(max_length=255, null=True, blank=True)
    is_admin = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return str(self.user.first_name) + " " + str(self.user.last_name)
