from rest_framework import serializers
from .models import Gatito

class GatitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gatito
        fields = '__all__'