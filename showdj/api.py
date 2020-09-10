from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers, models
from django.http import JsonResponse
from rest_framework.exceptions import PermissionDenied

class Show(generics.ListCreateAPIView):
    queryset = models.Show.objects.all()
    serializer_class = serializers.ShowSerializer
    def post(self, request, *args, **kwargs):
        user = request.POST.get('username')
        users = User.objects.filter(username=user)
        if not users.count() == 1:
            data = {'success': False, 'message': 'Your username is incorrect'}
            return JsonResponse(data)
        else:
            user = users.first()
        show = models.Show.objects.get(pk=self.kwargs["pk"])
        if not user.is_staff:
            raise PermissionDenied("You can not create a Show.")
        return super().post(request, *args, **kwargs)