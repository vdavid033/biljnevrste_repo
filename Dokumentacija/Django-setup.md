
API = Application Programming Interface – biblioteke, moduli, komponente i alati koji se koriste u kreiranju softvera i koji dopuštaju njihovu međusobnu komunikaciju na predefiniran način. Korištenjem API-ja omogućeno je kombiniranje različitih tehnologija. 
REST = REpresentational State Transfer – arhitektura koja koristi HTTP metode GET, POST, PUT, DELETE za prijenos podataka i rad s podacima.  
GET – koristi se dohvat resursa/podataka
POST – koristi se za slanje, dodavanje novog resursa/podatka 
PUT – koristi se za promjenu stanja nekog resursa/podatka
DELETE – koristi se za brisanje resursa/podataka
REST API (RESTful API) koristi uglavnom HTTP protokol za rad s podacima ili nekim resursom, preko GET, POST, PUT, DELETE HTTP metoda. 
Postoji nekoliko karakteristika REST API-ja: 
klijentsko-serverski pristup, protokol kojeg koristi je stateless – svi pozivi su međusobno neovisni, tj.ne ovise o povratnoj informaciji sa serverske strane, podaci se pohranjuju privremeno u cache, postoji jedinstveno sučelje vezano uz API layer, ali neovisno o bilo kojoj aplikaciji, počiva na višeslojnom modelu radi modularnosti i skalabilnosti, dopušta se slanje programskog koda na zahtjev, kroz API.
REST API vraća formatirani zapis u XML (EXtensible Markup Language), JSON (JavaScript Object Notation), YAML (YAML Ain't Markup Language) obliku.

Primjer:
•	Instalirati Django framework:
o	pip install django

•	Instalirati Django REST framework:
o	pip install djangorestframework

•	Kreirati Django projekt:
o	django-admin startproject biljnevrste
biljnevrste/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py

•	U folderu biljnevrste napraviti migraciju postojećeg modela i kreirati superusera:
o	python manage.py migrate
o	python manage.py createsuperuser

•	Kreirati aplikaciju biljnevrsteapp:
o	python manage.py startapp biljnevrsteapp


•	U settings.py dodati u instalirane aplikacije: rest_framework i biljnevrsteapp

•	U postojeći urls.py projekta dodati:
o	from django.urls import path, include
o	path('', include('biljnevrsteapp.urls'))


•	U urls.py aplikacije biljnevrsteapp 
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('biljnevrsteapp',views.BiljneVrsteView)

urlpatterns = [
	path('', include(router.urls))
]


•	U folderu biljnevrsteapp kreirati model
o	u models.py:
		class BiljneVrste(models.Model):
			naziv = models.CharField(max_length=100)
			vrsta = models.CharField(max_length=100)
			...
o	na temelju modela se radi baza
o	napraviti migraciju na bazu:
python manage.py makemigrations
python manage.py migrate

•	Startati server i unijeti URL u web preglednik za testiranje:
o	python manage.py runserver
o	http://127.0.0.1:8000/admin
o	Username/password (iooa/iooa11)

•	U folderu biljnevrsteapp ažurirati admin.py za prikaz administratorskog sučelja sa ovlastima:
o	U admin.py dodati:
from .models import BiljneVrste
admin.site.register(BiljneVrste)

•	U folderu biljnevrsteapp kreirati datoteku serializers.py za serijalizaciju podataka koji će biti bitni za unos/ispis podataka:
o	 Dodati:
from rest_framework import serializers
from .models import BiljneVrste

class BiljneVrsteSerializer(serializers.ModelSerializer):
	class Meta:
		model = BiljneVrste
		fields = ('id','naziv','vrsta')

•	U folderu biljnevrsteapp ažurirati views.py:
from django.shortcuts import render
from rest_framework import viewsets
from .models import BiljneVrste
from .serializers import BiljneVrsteSerializer

class BiljneVrsteView(viewsets.ModelViewSet):
	queryset = BiljneVrste.objects.all()
	serializer_class = BiljneVrsteSerializer


