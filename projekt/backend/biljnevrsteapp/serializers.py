from rest_framework import serializers
from .models import BiljneVrste
from rest_framework import viewsets

class BiljneVrsteSerializer(serializers.ModelSerializer):
	class Meta:
		model = BiljneVrste
		fields = ('id','naziv','vrsta','sinonim','opis')
