from email.policy import default
from rest_framework import serializers


class ItemSerializer(serializers.Serializer):
    id = serializers.IntegerField(default=None)
    hid = serializers.IntegerField(default=None)
    by = serializers.CharField(max_length=256, allow_null=True, default=None)
    kids =serializers.ListField(default=None, allow_empty=True)
    score = serializers.IntegerField(default=None)
    time = serializers.IntegerField(default=None)
    type = serializers.CharField(max_length=256, allow_null=True)
    deleted = serializers.BooleanField(default=False)
    dead = serializers.BooleanField(default=False)
    
    title = serializers.CharField(max_length=256, allow_null=True, default=None)
    descendants = serializers.IntegerField(default=None)
    url = serializers.URLField(max_length=512, allow_null=True, default=None)
    text = serializers.CharField(max_length=10000, allow_null=True, default=None)
    parts = serializers.ListField(default=None, allow_empty = True)