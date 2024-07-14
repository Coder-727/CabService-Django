# api/urls.py

from django.urls import path
from .views import (
    CabListCreate, CabRetrieveUpdateDestroy, LocationLastRecordView, 
    RideListCreate, RideRetrieveUpdateDestroy,
    UserListCreate, UserRetrieveUpdateDestroy, authenticate_user, locationListCreate, locationRetrieveUpdateDestroy
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('rides/', RideListCreate.as_view(), name='ride-list'),
    path('rides/<int:pk>/', RideRetrieveUpdateDestroy.as_view(), name='ride-detail'),
    path('users/', UserListCreate.as_view(), name='user-list'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroy.as_view(), name='user-detail'),
    # path('users/current/', get_current_user, name='current-user'), 
    path('users/authenticate/', authenticate_user, name='authenticate-user'),
    path('cabs/', CabListCreate.as_view(), name='cab-list'),
    path('cabs/<int:pk>/', CabRetrieveUpdateDestroy.as_view(), name='cab-detail'),
    path('location/', locationListCreate.as_view(), name='location-list'),
    path('location/<int:pk>/', locationRetrieveUpdateDestroy.as_view(), name='location-detail'),
    path('location/last/', LocationLastRecordView.as_view(), name='location-last'),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
