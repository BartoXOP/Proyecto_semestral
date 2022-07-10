from rest_framework import serializers
from .models import Perrito

class PerritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perrito
        fields = '__all__'