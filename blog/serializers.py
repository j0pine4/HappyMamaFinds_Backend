from rest_framework import serializers
from . import models

class BlogThumbnailSerializer(serializers.ModelSerializer):

    class Meta:
        depth = 1
        model = models.Post
        fields = [
            'id',
            'author',
            'title',
            'title_slug',
            'subtitle',
            'headerImage_url',
            'categories',
            'created_on',
        ]

class BlogPostSerializer(serializers.ModelSerializer):

    class Meta:
        depth = 1
        model = models.Post
        fields = [
            'id',
            'author',
            'title',
            'title_slug',
            'content',
            'subtitle',
            'headerImage_url',
            'categories',
            'tags',
            'created_on',
        ]
        lookup_field = 'title_slug'
        extra_kwargs = {
            'url': {'lookup_field': 'title_slug'}
        }