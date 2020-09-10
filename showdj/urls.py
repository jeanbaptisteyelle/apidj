from django.urls import path
from . import views, api

urlpatterns = [
    path('', views.show, name='show'),

# Routes API

    path('shows/<int:pk>', api.Show.as_view(), name='shows')

    ]
