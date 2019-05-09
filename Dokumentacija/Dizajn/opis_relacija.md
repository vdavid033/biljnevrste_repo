# Opisi relacija

SLIKA,
UPORABNI_DIO, 
UPORABNI_DIO_VRSTE


## SLIKA

ID_slike- PK, šifra slike, samonumeriranje, broj(12)

Naziv_slike - Tekst (50)

Opis_slike - Tekst(255)

ID_uporabni_dio - FK, vanjski kljuc, broj(12)

## UPORABNI_DIO

ID_uporabni_dio - PK, šifra slike, samonumeriranje, broj(12)

uporabni_dio - naziv uporanog djela, Tekst(100)


## UPORABNI_DIO_VRSTE
AGREGACIJA!

ID_uporabni_dio - vanjski kljuc, broj(12)

ID_biljna_vrsta - vanjski kljuc, broj(12)

## BILJNA_VRSTA

ID_biljne_vrste - PK, sifra vrste, samonumeriranje, broj(12)

hrvatski_naziv_vrste - tekst(100)

latinski naziv - tekst(100)

Sinonim_vrste - tekst(100)

Opis_vrste - tekst(255)

ID_roda - vanjski kljuc, broj(12)
ID_sistematicara - vanjski kljuc, broj(12)

## Rod
ID_roda - PK, samonumeriranje(12)  
Naziv_roda - Tekst(30)

## Porodica
ID_porodice - PK, samonumeriranje, broj(12)  
Hrvatski_naziv_porodice - Tekst(100)  
Latinski_naziv_porodice - Tekst(100)  
ID_roda - FK, broj(12)


## Sistematicar

ID_sistematicara -  PK, samonumeriranje, broj(12)   
Naziv_sistematicara - Tekst(100)

## Podvrsta
ID_podvrste - PK, samonumeriranje, broj(12)   
Naziv_podvrste - Tekst(100)  
ID_biljne_vrste- FK, broj(12)

## Varijet
ID_varijeta - PK, samonumeriranje, broj(12)  
Naziv_varijeta - Tekst(100)  
ID_podvrste - FK, broj(12)

