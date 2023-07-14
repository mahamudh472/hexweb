from rest_framework import serializers
from .models import *




class CoverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cover
        fields = ['name', 'price_per_day']