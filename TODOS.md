TODO: linki do manufacturera z poziomu product, cardproductmin itd

TODO: udynamicznianie:
[ ] ProductRight - funkcjonalnosci dodawania do koszyka, favorites, przechodzenia do koszyka:
[ ] endpoint dodawania produktu do koszyka
[ ] dodawanie do koszyka z strony produktu
[ ] dodawanie do koszyka z strony gridu
[ ] endpoint usuwania z koszyka
[ ] dynamiczna strona koszyka
[ ] usuwanie z koszyka z poziomu strony koszyka
[ ] koszyk jest zwiazany z produktami i uzytkownikiem, wiec kwestia przekazywania i aktualizacji w navie - moze dodac store na koszyk, zeby mogl byc aktualizowany z dowolnego miejsca
[ ] proby takiej wlasnie synchronizacji aktualizacji
[ ] zwiekszanie ilosci przedmiotow danego typu w z poziomu strony koszyka
[ ] z poziomu strony koszyka - jesli kliniemy dwukrotnie "dodaj do koszyka" to powinno dodac drugi raz itd?
[ ] dynamicznosc strony koszyka wlacznie z czy przedmioty w ulubionych?

TODO: aktualizacja view lajkowania - czy nie moge odbierac request usera w drf zamiast podawac jego nazwy w body?

TODO: realizacja poprzez API dodawania produktow do koszyka:
[ ] endpointy - cart zwiazany jest z uzytkownikiem, wiec w endpoincie sproboj wykorzystac request user a potem jego cart, a w tresci sprobuj przekazywac obiekt produktu (ale nie wiem czy mozliwe bo serializacja usera), a jak nie to po slugu
[ ] obluga na stronie produktu
[ ] dodac jakos do grid
[ ] na sklepie produktu przycisk "buy now" zeby dodawal do cartu i przechodzil do strony koszyka


TODO: koszyk dynamicznie
[ ] odbieranie danych o koszyku w navie - a moze jako czesc serializatora uzytkownika po prostu? ale wtedy koszyk musialby tez zawierac produkty itd, ale to ok, bo to jego integralna czesc
[ ] odbieranie danych na stronie koszyka
[ ] usuwanie z koszyka z poziomu strony koszyka - jesli jest wiele takich samych to jak precyzowac ktory usuwac itd..
[ ] tak samo zmienianie ilosci w koszyku - jak precyzowac
[ ] ogolnie zmienianie ilosci - najprosciej 1 przyciskiem typu +1, ale gdyby selectem, to by trzeba przekazywac ten numer i jaki produkt dodac
[ ] Na start wyswietlanie po prostu wszystkich jak leci, ale potem jesli ten sam produkt to niech Vue scala w jedno tylko z numerkiem
[ ] kwestia quantity - ilosc produktow w koszyku nie moze przekraczac dostepnej
[ ]


TODO: cos zrobic z user type?


FIXME: zabezpieczenia serializatorow itd - chuja troche

TODO: kwestia aplikowania styli typu wyszarzone w koszyku i dropdownie gdy quantity = 0 

TODO: customowe tosty (albo te co sa ale z wykorzystaniem slotu) przy dodawaniu do koszyka

TODO: moze jakis wspolny css dla vue i django globalny zeby te same kolory i inne

TODO: Nav w vue
    -> ~~stworz jakies manufacturer, product, order, konta, reviews~~
    -> Nav z fake danymi
    -> Nav z odbiorem danych o uzytkowniku, koszuku, logowanie
    -> Prosta strona produktu i dodawanie do koszyka i jak bedzie z aktualizacja tego (poprzez store i refs?)

TODO: API na:
    - get, patch produkt, get list product z paginacja i filtracja
    - get, patch profile
    - get, post, patch, delete review
    - get, patch cart

    a potem reszta dla kompletnosci?

TODO: 

Opcjonalne: OpenAPI client generator: tzn automatycznie generowane na podstawie schema API funkcje do odbierania z nich danych, przekazywanai itd - z minimalna iloscia pisania

https://www.saaspegasus.com/guides/modern-javascript-for-django-developers/apis/


TODO: Plan realizacji konwertowania wizualiów:

Generalnie w projekcie 'testy_designow/sklep_pedaly' mam zrealizowane 3/4 ukladu (home, product page, store page) tylko ze kompletnie statyczne - ale za to generalnie reactive, moze poza strona produktu z obrazkiem i contact form tez wystaje troche

W 'strona_front' sa jest tez designu troche, ale raczej outdated

W 'vue_blog' masz na przyklad realizacje ruchomego banneru w hero section - do wziecia