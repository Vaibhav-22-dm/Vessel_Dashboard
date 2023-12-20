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


SECRET = getattr(settings, 'SECRET', "secret")
ALGO = getattr(settings,'ALGO', 'HS256')

# Create your views here.
@api_view(['POST'])
@authentication_classes([CustomAuthentication])
def signup(request):
    try:
        username = request.data.get('username')
        password = request.data.get('password')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')
        phone_no = request.data.get('phone_no')
        device_id = request.data.get('device_id')
        owner = Employee.objects.get(user=request.user)

        if owner.is_admin == False:
            return Response({
                'error': 'You are not authorized to perform this action'
            }, status=401)
        
        user = User.objects.create(
            username=username, 
            first_name=first_name,
            last_name=last_name,
            email=email)
        user.set_password(password)
        user.save()

        employee = Employee.objects.create(user=user, port=owner.port, phone_no=phone_no, device_id=device_id)
        employee.save()

        return Response({
            'message':'Account created successfully'
        }, status=200)
        
    except Exception as e:
        return Response({'error': str(e)}, status=400)
    
@api_view(['POST'])
def signin(request):
    try:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            employee = Employee.objects.get(user=user)
            serializer = EmployeeSerializer(employee)
            payload = {
                "id": user.id,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=129600),
                "iat": datetime.datetime.utcnow(),
                "port_id": employee.port.id
            }
            token = jwt.encode(payload, SECRET, algorithm=ALGO)
            return Response({
                'message':'You have successfully logged in',
                'token':token,
                "employee": serializer.data
                }, 
                status=200)
    except Exception as e:
        return Response({'error': str(e)}, status=400)
