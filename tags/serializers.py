from rest_framework import serializers

from .models import URLmodel


class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URLmodel
        fields = ('__all__')


class TagsSerializer(serializers.Serializer):
    tags = serializers.DictField(
        child=serializers.CharField(max_length=100))


class ResponseSerializer(serializers.Serializer):
    response = serializers.CharField(max_length=100)
