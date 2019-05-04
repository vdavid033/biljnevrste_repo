
# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from .models import BiljneVrste
from .serializers import BiljneVrsteSerializer

class BiljneVrsteView(viewsets.ModelViewSet):
	queryset = BiljneVrste.objects.all()
	serializer_class = BiljneVrsteSerializer
