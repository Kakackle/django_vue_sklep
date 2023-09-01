TODO: przeniesienie plikow template z generalnych do app sklep

TODO: lepsza nazwa niz /vue, moze /sklep, bo pustego bym nie chcial...
ale puste jest duzo bardziej intuicyjne...
wiec cos na pustym by sie przydalo - cos stalego najlepiej, hmm

albo jakis redirect prowadzacy zawsze z "/" do "sklep/"? powinno byc mozliwe

TODO: Home view z hero i bannerem jako komponenty

TODO: project view

TODO: forms w django na manufacturer, produkt (z podgladem na obrazki), uzytkownika

TODO: moze jakis wspolny css dla vue i django globalny zeby te same kolory i inne

TODO: Nav w vue
    -> stworz jakies manufacturer, product, order, konta, reviews
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

TODO: 

Opcjonalne: OpenAPI client generator: tzn automatycznie generowane na podstawie schema API funkcje do odbierania z nich danych, przekazywanai itd - z minimalna iloscia pisania

https://www.saaspegasus.com/guides/modern-javascript-for-django-developers/apis/


TODO: Plan realizacji konwertowania wizualiów:

Generalnie w projekcie 'testy_designow/sklep_pedaly' mam zrealizowane 3/4 ukladu (home, product page, store page) tylko ze kompletnie statyczne - ale za to generalnie reactive, moze poza strona produktu z obrazkiem i contact form tez wystaje troche

W 'strona_front' sa jest tez designu troche, ale raczej outdated

W 'vue_blog' masz na przyklad realizacje ruchomego banneru w hero section - do wziecia