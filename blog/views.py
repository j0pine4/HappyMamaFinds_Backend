from . import models
from . import serializers
from rest_framework import viewsets, views
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from random import shuffle

# Create your views here.
class blogView(viewsets.ModelViewSet):
    queryset = models.Post.objects.filter(isPublished=True).order_by('-created_on')
    serializer_class = serializers.BlogPostSerializer
    lookup_field = 'title_slug'
    

class FeaturedBlogsView(views.APIView):
    def get(self, request):
        queryset = list(models.Post.objects.filter(isPublished=True))
        shuffle(queryset)
        serializer = serializers.BlogThumbnailSerializer(queryset[0:3], many=True)

        return Response(serializer.data)
    
class LatestBlogView(views.APIView):
    def get(self, request):
        queryset = models.Post.objects.filter(isPublished=True).latest('created_on')
        serializer = serializers.BlogThumbnailSerializer(queryset)

        return Response(serializer.data)