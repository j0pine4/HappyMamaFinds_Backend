from rest_framework import generics, views, viewsets
from rest_framework.response import Response
from . import serializers
from . import models
import os

from root import services

"""
Views for user API
"""

class CreateUserView(generics.CreateAPIView):
    """ Create a new user in the system """
    serializer_class = serializers.UserSerializer

class ContactFormView(viewsets.ModelViewSet):
    queryset = models.ContactForm.objects.all()
    serializer_class = serializers.ContactSerializer