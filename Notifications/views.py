from .models import *
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from Vessel_Dashboard.auth import CustomAuthentication
from .serializers import *

@api_view(['POST'])
@authentication_classes([CustomAuthentication])
def add_notification(request):
    try:
        notification = BroadcastNotification.objects.create(message=request.POST.get('message'),author=request.user)
        notification.save()
        return Response({
            'message' : 'Notification Created successfully'
        }, status=200)
    except Exception as e:
        return Response({'message':str(e)}, status=300)