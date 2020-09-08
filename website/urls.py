from django.urls import path, include
from rest_framework.authtoken import views

from rest_framework.routers import DefaultRouter
from . import api, views
router = DefaultRouter()
router.register('contact', api.ContactViewSet, basename='contact-api')
router.register('reseaux', api.ReseauxSociauViewSet, basename='reseaux-api')


urlpatterns = [
    path('', views.index, name='index'),
#les routes API
    path('team/<int:pk>', api.Our_team.as_view(), name='team'),
    path('about/<int:pk>', api.About.as_view(), name='about'),
    path('info/<int:pk>', api.Contact_info.as_view(), name='info'),
    path('newletter/<int:pk>', api.Newletter.as_view(), name='newletter'),

    path('login', api.Login.as_view(), name='login'),
    path('users', api.UserCreate.as_view(), name='user_create')

    ]
urlpatterns += router.urls