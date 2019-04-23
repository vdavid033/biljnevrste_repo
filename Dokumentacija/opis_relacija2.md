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