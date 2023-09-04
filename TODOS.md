TODO: kwestia dodawania do forms i views z Django przycisku cancel / cofania sie do home np

TODO: Postgres? Zeby miec np arrayfield

TODO: projekty wizualne cart view

TODO: cart view

TODO: strona na favorites poza po prostu filtrem "wyswietl ulubione"?

TODO: na stronie konta historia zamowien itd

TODO: strony manufacturera, usera itd

TODO: dropdown na cart

TODO: kwestia aplikowania styli typu wyszarzone w koszyku i dropdownie gdy quantity = 0 

TODO: dropdown na konto jest okej, tylko bez przesylania form a jedynie z user profile img, username i linki do logot, login, signup, user view (zrealziowane w Django)

TODO: customowe tosty (albo te co sa ale z wykorzystaniem slotu) przy dodawaniu do koszyka

TODO: moze jakies foldery w komponentach typu home/ , product/ itd zeby sobie segregowac

TODO: forms w django na manufacturer, produkt (z podgladem na obrazki) [ podglad mozliwy tylko dla edycji, tzn obrazki juz sa], uzytkownika

TODO: moze jakis wspolny css dla vue i django globalny zeby te same kolory i inne

TODO: Nav w vue
    -> ~~stworz jakies manufacturer, product, order, konta, reviews~~
    -> Nav z fake danymi
    -> Nav z odbiorem danych o uzytkowniku, koszuku, logowanie
    -> Prosta strona produktu i dodawanie do koszyka i jak bedzie z aktualizacja tego (poprzez store i refs?)

TODO: Store view

TODO: Order/Cart view

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