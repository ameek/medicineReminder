from rest_framework import serializers
from .models import Bucketlist

class BucketlistSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    class Meta:
        """this meta clss will map serializer's feilds with the model feilds"""
        model = Bucketlist
        feilds = ('id','name','date_created','date_modified')
        read_only_feilds = ('date_created', 'date_modified')
