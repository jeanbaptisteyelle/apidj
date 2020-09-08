from . import serializers, models
from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied

class Our_team(generics.ListCreateAPIView):
    queryset = models.Our_team.objects.all()
    serializer_class = serializers.Our_teamSerializer
    def post(self, request, *args, **kwargs):
        user = request.POST.get('username')
        users = User.objects.filter(username=user)
        if not users.count() == 1:
            datas = {'success': False, 'message': 'username is not correct'}
            return JsonResponse(datas)
        else:
            user = users.first()
        Our_team = models.Our_team.objects.get(pk=self.kwargs["pk"])
        if not user.is_staff:
            raise PermissionDenied("You can not create a team.")
        return super().post(request, *args, **kwargs)


class About(generics.ListCreateAPIView):
    queryset = models.About.objects.all()
    serializer_class = serializers.AboutSerializer
    def post(self, request, *args, **kwargs):
        user=User
        about = models.About.objects.get(pk=self.kwargs["pk"])
        if not request.user == user.username:
            raise PermissionDenied("You can not create an about.")
        return super().post(request, *args, **kwargs)


class Contact_info(generics.ListCreateAPIView):
    queryset = models.Contact_info.objects.all()
    serializer_class = serializers.Contact_infoSerializer
    def post(self, request, *args, **kwargs):
        user=User
        info = models.Contact_info.objects.get(pk=self.kwargs["pk"])
        if not request.user == user.username:
            raise PermissionDenied("You can not create a contact_info.")
        return super().post(request, *args, **kwargs)

class Contact(generics.CreateAPIView):
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer
    

class Newletter(generics.CreateAPIView):
    queryset = models.Newletter.objects.all()
    serializer_class = serializers.NewletterSerializer
    def destroy(self, request, *args, **kwargs):
        user=User
        newletter = models.Newletter.objects.get(pk=self.kwargs["pk"])
        if not request.user == user.username:
            raise PermissionDenied("You can not delete this Newletter.")
        return super().destroy(request, *args, **kwargs)


class ReseauxSociauViewSet(viewsets.ModelViewSet):
    querryset = models.ReseauxSociau.objects.all()
    serializer_class = serializers.ReseauxSociauSerializer
    def destroy(self, request, *args, **kwargs):
        user=User
        newletter = models.Newletter.objects.get(pk=self.kwargs["pk"])
        if not request.user == user.username:
            raise PermissionDenied("You can not delete this Newletter.")
        return super().destroy(request, *args, **kwargs)

class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = serializers.Userserializer

class Login(APIView):
    permission_classes = ()
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            return Response({'token': user.auth_token.key})
        else:
            return Response({'error': "Mauvaises informations d'identification"}, status=status.HTTP_404_BAD_REQUEST)
