from django.db import models

# Create your models here.
class BiljneVrste(models.Model):
	naziv = models.CharField(max_length=100)
	vrsta = models.CharField(max_length=100)

