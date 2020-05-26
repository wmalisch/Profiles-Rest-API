from rest_framework import serializers

class HelloSerizalizer(serializers.Serializer):
    """Serializers name field for testing our APIView"""
    name = serializers.CharField(max_length=10)
