from rest_framework import serializers
from.models import *

class Resumeserializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = '__all__'