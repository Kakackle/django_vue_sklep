TODO: Postgres? Zeby miec np arrayfield

TODO: linki do manufacturera z poziomu product, cardproductmin itd

TODO: przetestuj jakies dodawanie POST z poziomu Vue, moze review bo malo pol albo moze effecttype

TODO: wiecej serializatorow

TODO: zabezpieczenia serializatorow itd - chuja troche

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

TODO: pozniej: lajkowanie recenzji zeby uzytkownik mogl ocenic ich wartosc itd

TODO: 

Opcjonalne: OpenAPI client generator: tzn automatycznie generowane na podstawie schema API funkcje do odbierania z nich danych, przekazywanai itd - z minimalna iloscia pisania

https://www.saaspegasus.com/guides/modern-javascript-for-django-developers/apis/


TODO: Plan realizacji konwertowania wizualiów:

Generalnie w projekcie 'testy_designow/sklep_pedaly' mam zrealizowane 3/4 ukladu (home, product page, store page) tylko ze kompletnie statyczne - ale za to generalnie reactive, moze poza strona produktu z obrazkiem i contact form tez wystaje troche

W 'strona_front' sa jest tez designu troche, ale raczej outdated

W 'vue_blog' masz na przyklad realizacje ruchomego banneru w hero section - do wziecia