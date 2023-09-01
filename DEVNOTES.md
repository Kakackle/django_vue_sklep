# Devnotes

ogolnie: https://www.saaspegasus.com/guides/modern-javascript-for-django-developers/integrating-django-react/

## Obsluga path do vue i reszty w Django

Potencjalnie porzadane jest aby path do aplikacji Vue byl explicit, np /vue albo /sklep jesli projekt jest sklepem itd
Chociaz byc moze jest to nie do konca intuicyjne dla uzytkownika

ale, jesli chcemy miec konkretny poczatek sciezki, router musi to rozpoznawac

Aby mogl to robic, nalezy dac mu o tym znac

Majac vue.config.js mozna ustawic tam: https://stackoverflow.com/questions/66284893/how-do-you-control-your-publicpath-property-in-vue-config-js

jesli nie mozna podac w createWebHistory('/path')

# Uruchamianie projektu

1. uruchomienie venv z poziomu folderu calosciowego django_vue_pegasus
2. z folderu pegasus uruchomienie serwera django python manage.py runserver - wykrywa zmiany w plikach zwiazanych z pythonem
3. z tego samego folderu uruchomienie dev mode aplikacji 'npm run dev', ktora bedzie wykrywac zmiany ktore zaszly w plikach vue itd


# przesylanie uzytkownika spowrotem w Vue

niektore forms moga byc robione w pelni w Django

ale niektore chcialbym pewnie w Vue, bo bardziej dynamiczne i z Vue dane najlatrwiej zwracac poprzez API

jak jednak uzyskac zalogowanego uzytkownika w Vue i jak go zwracac?

wg. https://stackoverflow.com/questions/30203652/how-to-get-request-user-in-django-rest-framework-serializer
w serializatorze mozna uzyskac dostep do self.context['request'].user aby miec dostep do zalogowanego uzytkownika

natomiast endpoint odbierajacy dane przez API moze jakos tez tak z request.userem mogly by uzyskwiac dostep i zapisywac

# login_required() zwracajace 404?
konieczne jest w definicji url login dla login_view dodac trailing slash, tzn path to "login/", "logout/", "signup/" a nie bez "/"

# rozwazania co Django a co Vue

## forms - w Django czy Vue?
generalnie wiekszosc moglaby byc nawet w django - tzn edycja danych uzytkownika, dodawanie produktow, edycja ich itd

Natomiast w Vue rzeczy jak dodawanie komentarzy, dodawanie do koszyka, obsluga menu filtracji, pisanie recenzji i wybor ratingu na gwiazdkach

Realizacja paginacji tez nie jest trudna z DRF

## kwestia odbierania danych z backendu przez front
czesc moze byc przekazywana przez JSON parse - stalych albo zmieniajacych sie tylko w rzadkich momentach wymagajacyh przejscia do Django jak login itd

Co natomiast zeby nie powstal taki chaos z pobieraniem danych z API jak w vue_blog? Rozwaz, gdzie bedziesz chcial pobierac dane:

(uzytkownik w Nav)
w Home:
1. najwyzej gallery - obrazki z rzeczywistych produktow albo stale wizualium tylko

w Store view:
1. GET produktow wszystkich z paginacja
2. GET przy paginacji
3. GET przy filtracji po kategoriach z menu bocznego
4. GET przy filtracji po gornym menu
5. GET po produktach w favourite
6. PATCH userprofile zeby dodac do favourites

w Product view:
1. GET produktu
2. GET reviews
3. POST review
(potem)
4. DELETE, PATCH, review
5. PATCH cart (modyfikujacy tez quantity productu)

w Checkout/Cart view:
1. GET cartu
2. POST z nowym order jesli przejdzie
3. PATCH cartu jesli uzytkownik cos usunie z koszyka, zmieni ilosc itd

Natomiast wszystko z dodawaniem i edycja produktow, manufacturer, konto w Django, bo mozna tam ez tez zrobic podglady obrazkow itd

### Nav Django czy Vue?
bo Django jest blizej backendu więc aktualizacja koszyka, usera itd i np form na logowanie mozna by tam wcisnac z htmx?

Ale z drugiej strony Chcialbym tam miec mozliwosc otwierania koszyka, dropdownu dla uzytkownika itd, wiec Vue to ulatwi

a realizacje przechodzenia do view login i signup itd mozna latwo zrobic linkami albo sztywnymi albo przekazywanymi z Django do vue przez json parse

## Ostatecznie:
Nav - Vue
Konta:
    - view - Vue 
    - edycja - Django
Produkty:
    - dodawanie i edycja - Django
    - view - Vue
Manufacturer
    - tworzenie i edycja - Django
    - view - Vue
Komenty: wszystko Vue jako czesc view produktu
Order page: Vue
Logowanie itd - Django