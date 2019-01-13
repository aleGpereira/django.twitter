from .models import Tweet
from rest_framework import serializers


class TweetSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for Tweet object."""

    class Meta:
        model = Tweet
        fields = ('id', 'author', 'text')
