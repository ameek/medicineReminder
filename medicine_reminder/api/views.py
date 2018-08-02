#from django.shortcuts import render

from rest_framework import generics
from .serializers import BucketlistSerializer
from .models import Bucketlist

# Create your views here.
Class CreateView(generics.ListCreateAPIView):
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

    def perform_create(self, serializers):
        serializer.save()
