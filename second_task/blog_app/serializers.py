from rest_framework import serializers
from .models import Blog, Category
from django.contrib.auth.models import User


class BlogSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    # author_name = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = '__all__'

    # def get_author_name(self, obj):
        # return obj.author.username if obj.author else None
  

    def validate(self, value):
        return value


class CategorySerializer(serializers.ModelSerializer):

    category_name = serializers.CharField()
    category = BlogSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        exclude = ['id']


class DetailBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'blog_title', 'post_date', 'is_public']