from pyexpat import model
from rest_framework import serializers

from django.contrib.auth.models import User
from .models import Artical


class ArticalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artical
        fields = '__all__'