TODO: cos zrobic z user type? - trzeba by jakos na backendzie odczytywac z profilu i na tej podstawie udzielac permissions, ale problemy sa z tym

FIXME: zabezpieczenia serializatorow itd - chuja troche

FIXME: cos rzeczywiscie z darmowym shippingiem? jesli chodzi o backend prosta sprawa - jesli suma przekroczy jakas tam wartosc, to w order nie dodawaj do kosztu shippingu.
A na froncie? Tez mozesz sum_cost brac z koszyka i ustawiac itd

[Pagination]
TODO: z jakiegos powodu komponent Pagination nie chce dzialac ze stronami zwracanymi z axiosGetPaginated - tak jakby zwracalo puste i dlatego nie wyswietla - rozwiazac czemu problem

[Daty]
TODO: daty wszedzie brzydkie jak noc przez ten czas - jak to zalatwic na froncie?
np. w ProductReviewSection, w orders itd

[Nav]
TODO: oddzielnie link na konto (tylko dla zalogowanego) i user view (dla kazdego)
TODO: funkcjonalnosc zmieniania theme na dark na switchu... - widzialem to raz np. w postaci przygotowania dwoch zestawow zmiennych o takich samych nazwach odpowiadajacych uzywanym kolorom i te zestawy aplikowane zaleznie od klasy na root czy body czy cos

[ProductView i ogolnie]
TODO: i moze wszedzie: kolro czcionki zamiast czarnego jakis prawie-czarny

[Orders itd]
TODO: Generalnie pierdoli sie cos caly czas z suma przedmiotow, kosztow, discountami itd, trzeba sledzic w kazdym endpoincie - sprobuj dodac w metodzie save modeli
+ moze jakies properties

[ProductDescription]
TODO: dynamicznosc
TODO: funkcjonalnosc zmiany tabow
TODO: zrobic z tego ogolny komponent typu "tabs"? ze slotami, propami itd
TODO: w formie listy? ale to by trzeba jakos zapisywac w db ze to rozne przedmioty, idk

[ProductReviewSection]
TODO: paginacja 

[Footer]
TODO: kompletnie niekompletny

[Hero]
TODO: dynamicznosc na gridzie itd?
TODO: przyjmowanie danych z contact form do db?

[SimilarProducts]
TODO: dynamicznie i linki z nich do produktow ktore przedstawiaja


[dynamicznosc]
OrderView i inne
---------------
TODO: 

Opcjonalne: OpenAPI client generator: tzn automatycznie generowane na podstawie schema API funkcje do odbierania z nich danych, przekazywanai itd - z minimalna iloscia pisania

https://www.saaspegasus.com/guides/modern-javascript-for-django-developers/apis/
