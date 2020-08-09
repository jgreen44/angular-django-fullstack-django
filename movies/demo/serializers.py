from rest_framework import serializers
from .models import *


class CharactersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characters
        fields = [
            'id',
            'name'
        ]

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [
            'id',
            'name',
            'surname'
        ]


class BookNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookNumber
        fields = [
            'id',
            'isbn_13',
            'isbn_10',
        ]


class BookSerializer(serializers.ModelSerializer):
    number = BookNumberSerializer(many=False)
    characters = CharactersSerializer(many=True)
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'description',
            'price',
            'published',
            'is_published',
            'number',
            'characters',
            'authors'
        ]

class BookMiniSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = [
            'id',
            'title',
        ]
