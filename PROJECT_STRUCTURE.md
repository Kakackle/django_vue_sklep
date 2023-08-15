# Struktura projektu wytlumaczona

Projekt ma na celu polaczenie w jednym projekcie Django i Vue, w celu serwowania ich z jednego domain/portu/serweru

## Co to znaczy?

Podstawa projektu jest Django, ktore posiada jedno glowne View wykorzystujace template zawierajacy komponent, do ktorego przyczepiony jest root całego projektu Vue

Aktualnie jest on jeden, teoretycznie jednak mogłoby być ich wiele, możliwe jest również mieszanie view nie wykorzystujących Vue tylko samo Django z tymi wykorzystującymi

Dzięki przekazywaniu path w url do view z Vue, mozliwa jest takze obsluga Vue Routera


## Zalety

Mozliwosc korzystania z auth systemow Django

oraz pelnej funkcjonalnosci Vue, niedostepnej przy korzystaniu z Vue jako skrypt z CDN


## Struktura

Projekt zawiera kilka glownych podfolderow:

### front - frontend

Zawiera wszystkie pliki zwiazane z frontendem w Vue, w tym komponenty, views, router, assety

oraz plik **index.js**:

plik ten zawiera wskazanie do jakiego elementu na template przyczepic aplikacje, tworzy aplikacje Vue itd

### pegasus - glowny folder projektu Django

admin, urls itd

### static
index-bundle.js - wynikajacy plik kompilacji poprzez bundlowanie przez webpack i babel frontendu by mozliwe bylo do serwowania przez Django 

oraz inne pliki statyczne

### templates

- templates do view django


### sklep - Django app

w tym wypadku docelowym projektem jest sklep

obsluga funkcjonalnosci z tym zwiazanych, w tym API na bazie jego modeli oraz **glowne view VUE** - jest czescia tej apki, moglaby byc innej, gdyz powiazana jest z template **index.html** a nie konkretna Django app