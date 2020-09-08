from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers, models

from rest_framework.exceptions import PermissionDenied
class Show(generics.ListCreateAPIView):
    queryset = models.Show.objects.all()
    serializer_class = serializers.ShowSerializer
    def post(self, request, *args, **kwargs):
        user=User
        show = models.Show.objects.get(pk=self.kwargs["pk"])
        if not request.user == user.username:
            raise PermissionDenied("You can not create a Show.")
        return super().post(request, *args, **kwargs)