TODO: linki do manufacturera z poziomu product, cardproductmin itd

TODO: udynamicznianie:

TODO: czemu nie dziala dropdown adresow..... moze cos z kolenoscia, idk

TODO: z roznych poziomow dodawac linki do podstron manufacturerow, produktow itd

TODO: aktualizacja view lajkowania - czy nie moge odbierac request usera w drf zamiast podawac jego nazwy w body?


TODO: koszyk dynamicznie

[ ] kwestia quantity - ilosc produktow w koszyku nie moze przekraczac dostepnej - walidacja backendowa, bioraca przy zmienianiu ilosci dostepne quantity produktu i jesli byloby za duze to zwracajace 404 z wiadomoscia
[ ] - tostowanie a axios composables - zwracane jest aktualnie data i error - moge sprawdzic czy data i error sa null czy nie i na tej podstawie tostowac, tylko powtarzalna czynnosc - moze moge zrobic osobne composable na to, zeby wstawiac tosty tylko dla niektorych akcji 
[ ] tostowaie przy dodawaniu produktow do koszyka

TODO: orders
[ ] obsluga prawej strony - wpisywanie danych i dopisywanie do zamowienia...
ale jak obsluzyc adresy? bo powiedzmy ze mam shipping method, gdyby bylo rozdzielenie na np. paczkomaty oraz kuriera to roznica jak to przechowywac, ale jak tylko wersje kuriera z adresem to latwiej
[x] adres - moze dodatkowy model na adres z polami kraj, ulice, numer, kod pocztowy, ktory mozna (ale nie jest to wymagane) laczyc z profilem
[x] potem w order tez powiazanie z adresem
[x] serializatory w order cart items, adres, discount code?
[ ] podczas konwersji koszyka na order - zaznaczanie "uzyj swojego adresu" i wtedy stworzy nowy order z tym, a jesli nie, to sprobuje stworzyc z wypelnionych pol nowego adresu
[ ] konwersja cart na order - przekazywanie itemow (nie produktow), uzytkownika, automatycznie data, status domyslnie in progress, suma przedmiotow i..
[ ] konwersja ceny calego koszyka - suma cen po ich wlasnych discountach, mnozona stosownie przez quantity z item +..
[x] discount code - input na tekst i jak sprawdzic czy kod istnieje? moze dodatkowy model na discount, ktory bedzie zawieral nazwe/kod, wartosc discountu, date do ktorej jest wazny
[x] serializatory discount itd
[ ] i potem dac obok inputu na kod przycisk, ktory bedzie wysylal do endpointu wpisany tekst i sprawdzal czy istnieje taki kod i jesli tak, to zapisywal to jako czesc cart albo order, w ogolnym polu "discount" czy cos - chyba cart, zeby potem cene przeliczalo na order juz calkowita
[ ] po stworzeniu nowego obiektu order oproznic cart?

TODO: cos zrobic z user type? - trzeba by jakos na backendzie odczytywac z profilu i na tej podstawie udzielac permissions, ale problemy sa z tym

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