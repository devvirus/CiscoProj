from rest_framework import serializers
from .models import RouterDetails


class RouterSerializer(serializers.Serializer):
    Sapid = serializers.CharField(max_length=18)
    Host_name = serializers.CharField(max_length=14)
    Loop_back = serializers.CharField()
    Mac_address = serializers.CharField(max_length=14)

    def create(self, validated_data):
        return RouterDetails.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.Sapid = validated_data.get('Sapid', instance.Sapid)
        instance.Host_name = validated_data.get('Host_name', instance.Host_name)
        instance.Loop_back = validated_data.get('Loop_back', instance.Loop_back)
        instance.Mac_address = validated_data.get('Mac_address', instance.Mac_address)

        instance.save()
        return instance

