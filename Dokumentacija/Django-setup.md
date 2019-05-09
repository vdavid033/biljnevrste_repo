
**API** = Application Programming Interface – biblioteke, moduli, komponente i alati koji se koriste u kreiranju softvera i koji dopuštaju njihovu međusobnu komunikaciju na predefiniran način. Korištenjem API-ja omogućeno je kombiniranje različitih tehnologija.

**REST** = REpresentational State Transfer – arhitektura koja koristi HTTP metode GET, POST, PUT, DELETE za prijenos podataka i rad s podacima.

**GET** – koristi se dohvat resursa/podataka

**POST** – koristi se za slanje, dodavanje novog resursa/podatka

**PUT** – koristi se za promjenu stanja nekog resursa/podatka

**DELETE** – koristi se za brisanje resursa/podataka

**REST API (RESTful API)** koristi uglavnom HTTP protokol za rad s podacima ili nekim resursom, preko GET, POST, PUT, DELETE HTTP metoda. 

Postoji nekoliko karakteristika REST API-ja: 

klijentsko-serverski pristup, protokol kojeg koristi je stateless – svi pozivi su međusobno neovisni, tj.ne ovise o povratnoj informaciji sa serverske strane, podaci se pohranjuju privremeno u cache, postoji jedinstveno sučelje vezano uz API layer, ali neovisno o bilo kojoj aplikaciji, počiva na višeslojnom modelu radi modularnosti i skalabilnosti, dopušta se slanje programskog koda na zahtjev, kroz API.

REST API vraća formatirani zapis u XML (EXtensible Markup Language), JSON (JavaScript Object Notation), YAML (YAML Ain't Markup Language) obliku.



* Instalirati Django framework:

*pip install django*

* Instalirati Django REST framework:

*pip install djangorestframework*

* Kreirati Django projekt:

*django-admin startproject biljnevrste*

```
	biljnevrste/
	    manage.py
	    mysite/
	        __init__.py
	        settings.py
	        urls.py
	        wsgi.py
```

* U folderu biljnevrste napraviti migraciju postojećeg modela 

*python manage.py migrate*

* kreirati superusera:

*python manage.py createsuperuser*

* Kreirati aplikaciju biljnevrsteapp:

*python manage.py startapp biljnevrsteapp*

* U settings.py dodati u instalirane aplikacije: rest_framework i biljnevrsteapp

* U postojeći urls.py projekta dodati:

```
    from django.urls import path, include
    path('', include('biljnevrsteapp.urls'))
```

* U urls.py aplikacije biljnevrsteapp 

```
	from django.urls import path, include
	from . import views
	from rest_framework import routers
	
	router = routers.DefaultRouter()
	router.register('biljnevrsteapp',views.BiljneVrsteView)
	
	urlpatterns = [
		path('', include(router.urls))
	]
	
```

* U folderu biljnevrsteapp kreirati model

* U models.py:

```
	class BiljneVrste(models.Model):
		naziv = models.CharField(max_length=100)
		vrsta = models.CharField(max_length=100)
		...
```

* na temelju modela se radi baza

* napraviti migraciju na bazu:

*python manage.py makemigrations*

*python manage.py migrate*

* Startati server i unijeti URL u web preglednik za testiranje:

*python manage.py runserver*

http://127.0.0.1:8000/admin

Username/password (iooa/iooa11)

* U folderu biljnevrsteapp ažurirati admin.py za prikaz administratorskog sučelja sa ovlastima:

U admin.py dodati:

```
	from .models import BiljneVrste
	admin.site.register(BiljneVrste)
```

* U folderu biljnevrsteapp ažurirati views.py:

```
from django.shortcuts import render
from rest_framework import viewsets
from .models import BiljneVrste
from .serializers import BiljneVrsteSerializer

class BiljneVrsteView(viewsets.ModelViewSet):
	queryset = BiljneVrste.objects.all()
	serializer_class = BiljneVrsteSerializer
```

