from django.contrib.auth.models import User
from rest_framework import viewsets

# Create your views here.
from apps.profiles.models import Profile
from apps.profiles.serializers import ProfileSerializer, UserSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
