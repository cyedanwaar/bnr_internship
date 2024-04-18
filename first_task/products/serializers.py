from rest_framework import serializers
from .models import Product

import re
regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['slug', 'name', 'price']
    
    def validate_slug(self, value):

        if len(value.strip()) < 1:
            raise serializers.ValidationError("Slug cannot be empty")
        
        if Product.objects.all().filter(slug__contains=value).exists():
            raise serializers.ValidationError("Slug Already Exists")
        
        return value.strip()
    
    def validte_name(self, value):
        if len(value.strip()) < 1:
            raise serializers.ValidationError("Product Name is required")
        
        if regex.search(value):
            raise serializers.ValidationError("Product Name cannot contain special characters")
        
        return value.strip()
    
    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Product price must be greater than 0")
        
        return value