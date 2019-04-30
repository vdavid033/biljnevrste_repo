from django.db import models

# Create your models here.
class Slika(models.Model):
    ID_slike = models.AutoField(primary_key=True)
    naziv_slike = models.CharField(max_length=50)
    opis_slike = models.CharField(max_length=255)
    ID_uporabni_dio = models.ForigenKey(Uporabni_dio)

class Uporabni_dio(models.Model):
    ID_uporabni_dio = models.AutoField(primary_key=True)
    uporabni_dio = models.CharField(max_length=100)

class Uporabni_dio_vrste(models.Model):
    ID_uporabni_dio = models.ForigenKey(Uporabni_dio)
    ID_biljna_vrsta = models.ForigenKey(Biljna_vrsta)

class Biljna_vrsta(models.Model):
    ID_biljne_vrste = models.AutoField(primary_key=True)
    hrvatski_naziv_vrste =  models.CharField(max_length=100)
    latinski_naziv =  models.CharField(max_length=100)
    sinonim_vrste = models.CharField(max_length=100)
    opis_vrste =  models.CharField(max_length=255)
    ID_roda = models.ForigenKey(Rod)

class Rod(models.Model):
    ID_roda = models.AutoField(primary_key=True)
    naziv_roda =  models.CharField(max_length=30)

class Porodica(models.Model):
    ID_porodice = models.AutoField(primary_key=True)
    hrvatski_naziv_porodice =  models.CharField(max_length=100)
    latinski_naziv_porodice =  models.CharField(max_length=100)
    ID_roda = models.ForigenKey(Rod)

class Sistematicar(models.Model):
    ID_sistematicara = models.AutoField(primary_key=True)
    naziv_sistematicara = models.CharField(max_length=100)

class Podvrsta(models.Model):
    ID_podvrste = models.AutoField(primary_key=True)
    naziv_podvrste = models.CharField(max_legth=100)
    ID_biljne_vrste =models.ForeignKey(Biljna_vrsta)

class Varijet(models.Model):
    ID_varijeta = models.AutoField(primary_key=True)
    naziv_varijeta = models.CharField(max_length=100)
    ID_podvrste = models.ForeignKey(Podvrsta)




    # auto models.AutoField(primary_key=True)
    # char models.CharFiled(max_length=)
    # vanjski models.ForigenKey(ime_klase)
    #