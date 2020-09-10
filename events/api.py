from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from . import serializers, models

from rest_framework.exceptions import PermissionDenied

class Event(generics.ListCreateAPIView):
    queryset = models.Event.objects.all()
    serializer_class = serializers.Eventserializer
    def post(self, request, *args, **kwargs):
        user = request.POST.get('username')
        users = User.objects.filter(username=user)
        if not users.count() == 1:
            data = {'success': False, 'message':'your username is incorrect'} 
            return JsonResponse(data)
        else:
            user = users.first()
        Event = models.Event.objects.get(pk=self.kwargs["pk"])
        if not user.is_staff:
            raise PermissionDenied("You can't create an event.")
        return super().post(request, *args, **kwargs)