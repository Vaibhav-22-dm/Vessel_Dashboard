from .models import *
from rest_framework import serializers

class NotificationSerializer(serializers.ModelSerializer):
    timestamp = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    class Meta:
        model = BroadcastNotification
        fields = ['id','message', 'title', 'category']
    
    