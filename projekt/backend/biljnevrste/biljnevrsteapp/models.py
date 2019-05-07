from django.db import models

# Create your models here.
class Rod(models.Model):
    ID_roda = models.AutoField(primary_key=True)
    naziv_roda =  models.CharField(max_length=30)

class Uporabni_dio(models.Model):
    ID_uporabni_dio = models.AutoField(primary_key=True)
    uporabni_dio = models.CharField(max_length=100)

class Sistematicar(models.Model):
    ID_sistematicara = models.AutoField(primary_key=True)
    naziv_sistematicara = models.CharField(max_length=100)

class Slika(models.Model):
    ID_slike = models.AutoField(primary_key=True)
    naziv_slike = models.CharField(max_length=50)
    opis_slike = models.CharField(max_length=255)
    ID_uporabni_dio = models.ForeignKey(Uporabni_dio, on_delete=models.CASCADE)

class Biljna_vrsta(models.Model):
    ID_biljne_vrste = models.AutoField(primary_key=True)
    hrvatski_naziv_vrste =  models.CharField(max_length=100)
    latinski_naziv =  models.CharField(max_length=100)
    sinonim_vrste = models.CharField(max_length=100)
    opis_vrste =  models.CharField(max_length=255)
    ID_roda = models.ForeignKey(Rod, on_delete=models.CASCADE)

class Uporabni_dio_vrste(models.Model):
    ID_uporabni_dio = models.ForeignKey(Uporabni_dio, on_delete=models.CASCADE)
    ID_biljna_vrsta = models.ForeignKey(Biljna_vrsta, on_delete=models.CASCADE)

class Porodica(models.Model):
    ID_porodice = models.AutoField(primary_key=True)
    hrvatski_naziv_porodice =  models.CharField(max_length=100)
    latinski_naziv_porodice =  models.CharField(max_length=100)
    ID_roda = models.ForeignKey(Rod, on_delete=models.CASCADE)


class Podvrsta(models.Model):
    ID_podvrste = models.AutoField(primary_key=True)
    naziv_podvrste = models.CharField(max_length=100)
    ID_biljne_vrste =models.ForeignKey(Biljna_vrsta, on_delete=models.CASCADE)

class Varijet(models.Model):
    ID_varijeta = models.AutoField(primary_key=True)
    naziv_varijeta = models.CharField(max_length=100)
    ID_podvrste = models.ForeignKey(Podvrsta, on_delete=models.CASCADE)



    # auto models.AutoField(primary_key=True)
    # char models.CharFiled(max_length=)
    # vanjski models.ForigenKey(ime_klase)
    #
