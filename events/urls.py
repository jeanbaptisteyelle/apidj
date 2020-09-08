from django.urls import path
from . import api, views

urlpatterns = [
  path('', views.dj, name='dj'),
  path('events', views.events, name='events'),
  path('single', views.single, name='single'),
  path('about', views.about, name='about'),
  path('contact', views.contact, name='contact'),




# routes API

  path('event/<int:pk>', api.Event.as_view(), name='event'),
  ]