from . import models
from . import serializers
from rest_framework import viewsets, views
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from random import shuffle
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

# Create your views here.
class blogView(viewsets.ModelViewSet):
    queryset = models.Post.objects.select_related('author').prefetch_related('categories').filter(isPublished=True).order_by('-created_on')
    serializer_class = serializers.BlogPostSerializer
    lookup_field = 'title_slug'

    @method_decorator(cache_page(60*60*2))
    def list(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)
    

class FeaturedBlogsView(views.APIView):
    @method_decorator(cache_page(60*60*2))
    def get(self, request):
        queryset = models.Post.objects.select_related('author').prefetch_related('categories').filter(isPublished=True).only('author', 'title', 'title_slug', 'subtitle', 'headerImage_url', 'categories', 'created_on').order_by('?')[0:3]
        serializer = serializers.BlogThumbnailSerializer(queryset, many=True)

        return Response(serializer.data)
    
class LatestBlogView(views.APIView):
    @method_decorator(cache_page(60*60*2))
    def get(self, request):
        queryset = models.Post.objects.select_related('author').prefetch_related('categories').filter(isPublished=True).only('author', 'title', 'title_slug', 'subtitle', 'headerImage_url', 'categories', 'created_on').latest('created_on')
        serializer = serializers.BlogThumbnailSerializer(queryset)

        return Response(serializer.data)