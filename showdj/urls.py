from django.urls import path
from . import views, api

urlpatterns = [
    path('', views.show, name='show'),

# Routes API


    path('show/<int:pk>', api.Show, name='show')

    ]
