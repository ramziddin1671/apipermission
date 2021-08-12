from .models import Partfolio
from rest_framework import serializers


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partfolio
        fields = '__all__'
