from django.urls import path, include
from rest_framework.authtoken import views
from . import api, views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('reseaux', api.ReseauxSociauViewSet, basename='reseaux-api')

urlpatterns = [
    path('', views.index, name='index'),
#les routes API
    path('contact', api.Contact, name='contact'),

    path('team/<int:pk>', api.Our_team.as_view(), name='team'),
    path('about/<int:pk>', api.About.as_view(), name='about'),
    path('info/<int:pk>', api.Contact_info.as_view(), name='info'),
    path('newletter/<int:pk>', api.Newletter.as_view(), name='newletter'),

    path('login', api.Login.as_view(), name='login'),
    path('users', api.UserCreate.as_view(), name='user_create'),

    path("api/", include(router.urls))
    ]
