from django.db import models

# Create your models here.
class Rod(models.Model):
    ID_roda = models.AutoField(primary_key=True)
    naziv_roda =  models.CharField(max_length=30)
	
	class Meta:
		verbose_name = "Rod"
		verbose_name_plural = "Rodovi"

	def __str__(self):
		return self.naziv_roda

class Uporabni_dio(models.Model):
    ID_uporabni_dio = models.AutoField(primary_key=True)
    uporabni_dio = models.CharField(max_length=100)

	class Meta:
		verbose_name = "Uporabni dio"
		verbose_name_plural = "Uporabni djelovi"

	def __str__(self):
		return self.uporabni_dio


class Sistematicar(models.Model):
    ID_sistematicara = models.AutoField(primary_key=True)
    naziv_sistematicara = models.CharField(max_length=100)

	class Meta:
		verbose_name = "Sistematicar"
		verbose_name_plural = "Sistematicari"

	def __str__(self):
		return self.naziv_sistematicara

class Slika(models.Model):
    ID_slike = models.AutoField(primary_key=True)
    naziv_slike = models.CharField(max_length=50)
    opis_slike = models.CharField(max_length=255)
    ID_uporabni_dio = models.ForeignKey(Uporabni_dio, on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Slika"
		verbose_name_plural = "Slike"

	def __str__(self):
		return self.naziv_slike

class Biljna_vrsta(models.Model):
    ID_biljne_vrste = models.AutoField(primary_key=True)
    hrvatski_naziv_vrste =  models.CharField(max_length=100)
    latinski_naziv =  models.CharField(max_length=100)
    sinonim_vrste = models.CharField(max_length=100)
    opis_vrste =  models.CharField(max_length=255)
    ID_roda = models.ForeignKey(Rod, on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Biljna vrsta"
		verbose_name_plural = "Biljne vrste"

	def __str__(self):
		return self.hrvatski_naziv_vrste

class Uporabni_dio_vrste(models.Model):
    ID_uporabni_dio = models.ForeignKey(Uporabni_dio, on_delete=models.CASCADE)
    ID_biljna_vrsta = models.ForeignKey(Biljna_vrsta, on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Uporabni dio vrste"
		verbose_name_plural = "Uporabni djelovi vrste"

	def __str__(self): 
		return self.ID_uporabni_dio
		return self.ID_biljna_vrsta 

class Porodica(models.Model):
    ID_porodice = models.AutoField(primary_key=True)
    hrvatski_naziv_porodice =  models.CharField(max_length=100)
    latinski_naziv_porodice =  models.CharField(max_length=100)
    ID_roda = models.ForeignKey(Rod, on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Porodica"
		verbose_name_plural = "Porodice"

	def __str__(self):
		return self.hrvatski_naziv_porodice


class Podvrsta(models.Model):
    ID_podvrste = models.AutoField(primary_key=True)
    naziv_podvrste = models.CharField(max_length=100)
    ID_biljne_vrste =models.ForeignKey(Biljna_vrsta, on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Podvrsta"
		verbose_name_plural = "Podvrste"

	def __str__(self):
		return self.naziv_podvrste

class Varijet(models.Model):
    ID_varijeta = models.AutoField(primary_key=True)
    naziv_varijeta = models.CharField(max_length=100)
    ID_podvrste = models.ForeignKey(Podvrsta, on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Varijet"
		verbose_name_plural = "Varijeteti"

	def __str__(self):
		return self.naziv_varijeta



    # auto models.AutoField(primary_key=True)
    # char models.CharFiled(max_length=)
    # vanjski models.ForigenKey(ime_klase)
    #

