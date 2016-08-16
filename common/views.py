from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.permissions import AllowAny
from django.http import JsonResponse
from common.models import User
from common.serializers import UserSerializer
from datetime import datetime, date


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
