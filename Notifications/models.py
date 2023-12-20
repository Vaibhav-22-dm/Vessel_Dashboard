from django.db import models
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json
from django.contrib.auth.models import User

# Create your models here.

class BroadcastNotification(models.Model):

    CAT_CHOICES = (
        ('Alert','Alert'),
        ('Information','Information'),
        ('Updates','Updates'),
    )
    
    title = models.TextField(max_length=255, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=255, choices=CAT_CHOICES, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.title) + str(self.message) + str(self.category) + "~" + str(self.author.first_name)
    
    def save(self, *args, **kwargs):
        channel_layer = get_channel_layer()
        data = {'current_notification':{'message':self.message, 'title':self.title, 'category':self.category}}
        
        async_to_sync(channel_layer.group_send)(
            'notification_group',{
                'type':'send_notification',
                'value':json.dumps(data)
            }
        )
        
        super(BroadcastNotification, self).save(*args, **kwargs)

