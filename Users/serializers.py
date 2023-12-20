from rest_framework import serializers
from .models import *

class EmployeeSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.CharField(source='user.email')

    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'email', 'port', 'phone_no', 'device_id']
