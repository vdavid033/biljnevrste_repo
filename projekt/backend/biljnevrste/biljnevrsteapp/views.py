
# Create your views here.
# from django.shortcuts import render
# from rest_framework import viewsets
# from .models import Biljna_vrsta
# # from .serializers import BiljneVrsteSerializer
#
# class BiljneVrsteView(viewsets.ModelViewSet):
# 	queryset = BiljnaVrsta.objects.all()
# 	# serializer_class = BiljneVrsteSerializer

from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('HELLO FROM POSTS')

