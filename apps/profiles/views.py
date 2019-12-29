from django.contrib.auth.models import User
from rest_framework import viewsets

# Create your views here.
from apps.profiles.models import Profile, Role
from apps.profiles.serializers import ProfileSerializer, UserSerializer, RoleSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
