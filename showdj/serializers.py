from rest_framework import serializers
from . import models

class ShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Show
        fields = '__all__'
        