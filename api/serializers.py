from rest_framework import serializers
from api.models import RowPermitData


class RowPermitDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = RowPermitData
        fields = '__all__'

