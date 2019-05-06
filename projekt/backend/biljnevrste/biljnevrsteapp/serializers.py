from rest_framework import serializers
from .models import BiljneVrste

class BiljneVrsteSerializer(serializers.ModelSerializer):
	class Meta:
		model = BiljneVrste
		fields = ('id','naziv','vrsta','sinonim')
