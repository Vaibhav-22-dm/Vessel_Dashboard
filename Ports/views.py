from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, permission_classes, authentication_classes, parser_classes
from Vessel_Dashboard.auth import CustomAuthentication
from rest_framework.response import Response
from django.contrib.auth import authenticate
import jwt
import datetime
from django.conf import settings
from .serializers import *
from Users.models import *

# Create your views here.
@api_view(['POST'])
def create_port(request):
    try:
        name = request.data.get('name')
        lat = request.data.get('lat')
        long = request.data.get('long')
        dock_system = request.data.get('dock_system')

        if Port.objects.filter(name=name).first() is not None:
            return Response({
                "message": "Port already exists"
            }, status=403)
    
        username = request.data.get('username')
        password = request.data.get('password')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')
        
        user = User.objects.create(username=username, first_name=first_name, last_name=last_name, email=email)
        user.set_password(password)
        user.save()        

        port = Port.objects.create(name=name, lat=lat, long=long, dock_system=dock_system)
        port.save()

        phone_no = request.data.get('phone_no')
        device_id = request.data.get('device_id')

        employee = Employee.objects.create(user=user, port=port, phone_no=phone_no, device_id=device_id, is_admin=True)
        employee.save()

        return Response({
            'message': 'Account created successfully'
        }, status=200)

    except Exception as e:
        return Response({
            'error': str(e)
        }, status=400)

@api_view(['POST'])
@authentication_classes([CustomAuthentication])
def create_vessel(request):
    try:
        mmsi = request.data.get('mmsi')
        length = request.data.get('length')
        breadth = request.data.get('breadth')
        draft = request.data.get('draft')
        nationality = request.data.get('nationality')
        type = request.data.get('type')
        dwt = request.data.get('dwt')

        employee = Employee.objects.get(user=request.user)

        vessel = Vessel.objects.create(
            mmsi=mmsi, 
            length=length, 
            breadth=breadth, 
            draft=draft, 
            nationality=nationality, 
            type=type, 
            dwt=dwt,
            port=employee.port 
            )
        vessel.save()

        return Response({
            'message': 'Vessel created successfully'
        }, status=200)

    except Exception as e:
        return Response({
            'error': str(e)
        }, status=400)
    
@api_view(['GET'])
@authentication_classes([CustomAuthentication])
def get_port(request, pk):
    try:
        port = Port.objects.get(id=pk)
        serializer = PortSerializer(port)
        return Response({
            'port': serializer.data
        }, status=200)
    except Exception as e:
        return Response({
            'error': str(e)
        }, status=400)
    

@api_view(['GET'])
@authentication_classes([CustomAuthentication])
def get_ports(request):
    try:
        ports = Port.objects.all()
        serializer = PortSerializer(ports, many=True)
        return Response({
            'ports': serializer.data
        }, status=200)
    except Exception as e:
        return Response({
            'error': str(e)
        }, status=400)
    

@api_view(['GET'])
@authentication_classes([CustomAuthentication])
def get_vessel(request, pk):
    try:
        vessel = Vessel.objects.get(id=pk)
        serializer = VesselSerializer(vessel)
        return Response({
            'vessel': serializer.data
        }, status=200)
    except Exception as e:
        return Response({
            'error': str(e)
        }, status=400)

@api_view(['GET'])
@authentication_classes([CustomAuthentication])
def get_vessels(request):
    try:
        vessels = Vessel.objects.all()
        serializer = VesselSerializer(vessels, many=True)
        return Response({
            'vessels': serializer.data
        }, status=200)
    except Exception as e:
        return Response({
            'error': str(e)
        }, status=400)

@api_view(['GET'])
@authentication_classes([CustomAuthentication])
def get_port_vessels(request, pk):
    try:
        port = Port.objects.get(id=pk)
        vessels = Vessel.objects.filter(port=port)
        serializer = VesselSerializer(vessels, many=True)
        return Response({
            'vessels': serializer.data
        }, status=200)
    except Exception as e:
        return Response({
            'error': str(e)
        }, status=400)
