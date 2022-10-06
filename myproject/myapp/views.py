from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from .serializer import AdvSerializer

from .models import Adv
class AdvViewSet(ModelViewSet):
    queryset=Adv.objects.all()
    serializer_class=AdvSerializer