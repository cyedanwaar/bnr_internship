from rest_framework import serializers
from .models import Reference, BidderSupplier, Resource, ActivityDeliverable

class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reference
        fields = '__all__'


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityDeliverable
        fields = '__all__'


class BidderSerializer(serializers.ModelSerializer):
    resources = ResourceSerializer(many=True)
    activities = ActivitySerializer(many=True)
    class Meta:
        model = BidderSupplier
        fields = '__all__'
    
    def create(self, validated_data):
        
        resources_data = validated_data.pop('resources')
        activities_data = validated_data.pop('activities')

        bidder = BidderSupplier.objects.create(**validated_data)

        for resource in resources_data:
            Resource.objects.create(resource_bidder=bidder, **resource)
        
        for activity in activities_data:
            ActivityDeliverable.objects.create(activity_bidder=bidder, **activity)
        
        return bidder
    
   