# views.py

from rest_framework import generics
from .models import Ride, User, Cab, location
from .serializers import CabSerializer, RideSerializer, UserSerializer, locationSerializer

from django.http import JsonResponse

from rest_framework.decorators import api_view
from .models import User
from django.contrib.auth import authenticate
import logging
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes


# @permission_classes([IsAuthenticated])
class RideListCreate(generics.ListCreateAPIView):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer

class RideRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer

class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class locationListCreate(generics.ListCreateAPIView):
    queryset = location.objects.all()
    serializer_class = locationSerializer

class locationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = location.objects.all()
    serializer_class = locationSerializer

class LocationLastRecordView(generics.RetrieveAPIView):
    serializer_class = locationSerializer

    def get_queryset(self):
        return location.objects.order_by('-id')[:1]

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.first()
        return obj


# @permission_classes([IsAuthenticated])
class CabListCreate(generics.ListCreateAPIView):
    queryset = Cab.objects.all()
    serializer_class = CabSerializer


# @permission_classes([IsAuthenticated])
class CabRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cab.objects.all()
    serializer_class = CabSerializer
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)




import logging
import json  # Ensure json module is imported
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

# Configure logging
logger = logging.getLogger(__name__)

@api_view(['POST'])
def authenticate_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Username and password are required.'}, status=400)

    user = authenticate(username=username, password=password)

    if user is None:
        return Response({'error': 'Invalid username or password.'}, status=400)

    return Response({
        'message': 'Authentication successful',
        'is_driver': user.is_driver
    })

# @api_view(['POST'])
# def authenticate_user(request):
#     username = request.data.get('username')
#     password = request.data.get('password')

#     if not username or not password:
#         return Response({'error': 'Username and password are required.'}, status=400)

#     user = authenticate(username=username, password=password)

#     if user is None:
#         return Response({'error': 'Invalid username or password.'}, status=400)

#     refresh = RefreshToken.for_user(user)

#     return Response({
#         'refresh': str(refresh),
#         'access': str(refresh.access_token),
#         'is_driver': user.is_driver
#     })

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view(['POST'])
def create_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def get_current_user(request):
    
#     serializer = UserSerializer(request.user)
#     return Response(serializer.data)