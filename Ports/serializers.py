from rest_framework import serializers
from .models import *

class PortSerializer(serializers.ModelSerializer):

    class Meta:
        model = Port
        fields = '__all__'

class VesselSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vessel
        fields = '__all__'
