from rest_framework import serializers
from .models import Reference, BiderSupplier

class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reference
        fields = '__all__'
    

class BidderSerializer(serializers.ModelSerializer):
    class Meta:
        model = BiderSupplier
        fields = '__all__'
    
