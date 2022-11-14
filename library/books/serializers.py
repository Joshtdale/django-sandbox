from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Book, Category, Cuisine

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title']

class CuisineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuisine
        fields = ['title']


class BookSerializer(serializers.HyperlinkedModelSerializer):
    # categories = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    # categories = serializers.CharField(source='category.category.title')
    category = CategorySerializer()
    cuisine = CuisineSerializer()
    # category = serializers.ReadOnlyField(source='Category_title', allow_null=True)
    class Meta:
        model = Book
        fields = [
            'title',
            'published_year',
            'cuisine',
            'category'
            ]

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']