from dataclasses import field
from rest_framework import serializers

from .models import Adv
class AdvSerializer(serializers.ModelSerializer):
    class Meta:
        model=Adv
        fields=['title','decription']