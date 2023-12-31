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


# Przesylanie url obrazkow z django do vue (tak jakby) z django templates

Kiedy normalnie w template chcesz wyswietlic obrazek z Django z obrazkow na serwerze, robisz to poprzez src="{{jakis_obrazek.url}}", ale to wpisuje tam wtedy relative path tzn zaczynajacy sie od 'media/..' itd
a zeby to dzialalo z vue, jesli vue zaczyna sie od czegos jak '/sklep/' etc, trzeba podac w src caly path, bo jesli relative to dopisze po "sklep " etc i wyjdzie np "sklep/media/costam"

# Manualne tworzenie update forms 
Chyba ze chcesz wykluczyc jakies pole (uczynic "niezmienialnym"), mozesz uzyc tego samego Form oraz prawie tego samego view, wazna kwestia jest jednak by albo bawic sie z metodami .update, .update_fields, force_update albo po prostu w if request=='POST' poza request.POST przekazac tez instance = obiekt, bo Django zrozumie ktore pola wziac skad, nie konfliktuje


# kwestia edycji poszczegolnych obrazkow produktu zwiazanych z nimi, poprzez form:
zeby zamienic konkretny obrazek, musialbys miec dostep do dokladnie tego obiektu, tzn poprzez form zwiazany z tym dokladnie obiektem, ktore musialoby byc przesylane (submitowane) oddzielnie do aktualizacji

co mozna zrealizowac np poprzez wiele form w jednym view? i po przeslaniu tego form obrazka mogloby np wracac spowrotem do ogolnego form (tylko uwazac by zachowywac instance) i nawet wtedy powinno sie aktualziowac "real time" w miare? hmm

# unsafe methods przez DRF przy Vue serwowanym przez django, czyli defacto Django / same origin / domain
odpowiedz:
https://stackoverflow.com/questions/32653518/django-rest-framework-returning-403-response-on-post-put-delete-despite-allowa

same origin / domain zalatwia kwestie CORS

problemm jest jednak CSRF - ktory przesylasz zawsze w forms

potencjalnie pomyslalbys, ze wylaczenie 'django.middleware.csrf.CsrfViewMiddleware' w ustawieniach rozwiazalobvy sprawe - nope, i tak sprawdza

moze ustawienie dekoratora @csrf_exempt? - nope, nadal sprawdza

moze ustawienie w CRSF_TRUSTED_ORIGINS? - nope, nadal sprawdza

przesylanie w tresci 'csrfmiddlewaretoken'? Nope, nadal sprawdza

**jedyne co rozwiazalo to:** dodanie headera z tokenem 'X-CSRFToken': "Gd7syxIww0Krspr1IPqYi1Eq4vPNtQc3uBQeXkcInpeO05Clex6QQMZkaGxWR22E" do requestu

tylko że, co <span style="color:red">**giga wazne**</span> za kazdym razem (tzn przy kazdym refreshu strony, co jest czesto) trzeba wygenerowac nowy, co mozna dokonac metoda get_token(request) z from django.middleware.csrf import get_token, ktora zalezy wlasnie od requestu, a request po refreshu jest wlasnie inny

potencjalnie, robiac to Django serving Vue mozna by jakos uzyskac ten token w Django i przesylac go do Vue przez view, ale dodawanie odbierania tokenu przed kazdym patch/put/post nie jest trudne, wystarczy odebrac z endpointu /api/get_token i dokonywac  czynnosci zamierzone w .then

+ potencjalnie, wedlug docsow django, przy POST requestach konieczne moze byc dodanie "A hidden form field with the name ‘csrfmiddlewaretoken’, present in all outgoing POST forms.", czyli rowniez odbieranie tokenu i przesylanie razem z danymi POST


# drf custom object permissions - zeby dzialalo

zeby dzialalo, nie wystarczy napisac swojej wlasnej klasy permissions z metoda has_object_permissions sprawdzajacej czy np. obj.owner == request.user (jesli istnieje takie pole jak owner przypisane do modelu User na modelu sprawdzanym)
- trzeba rowniez zawrzec metode has_persmissions, np.

```
def has_permission(self, request, view):
    if request.method in permissions.SAFE_METHODS:
        print('safe')
        return True
    # return super().has_permission(request, view)
```
bo inaczej omija cala klase i nic nie sprawdza...

otoz nie:
---------------

probowalem wielu kombinacji, z jakiegos powodu nie chcialy dzialac, mimo ze powinno przepuszczac przez has_permissions i isc dalej

ale jedyne co zadzialalo to ustawienie has_permissions na:
```
def has_permission(self, request, view):
    return super().has_permission(request, view)
```

a potem pisanie swojego has_object_permissions

# laczenie wielu permissions
piszac permission_classes = (jedna, druga, itd) bedzie oczekiwalo, ze spelni wszystkie

ale zamiast tego mozna napisac = (jedna | druga | ) czyli dokonywac oberacji binarnych, w tym wypadku OR
https://www.revsys.com/tidbits/tip-about-drf-permissions/

# Filtracja z django_filters - customowe filtry klasy

https://django-filter.readthedocs.io/en/stable/guide/usage.html

https://django-filter.readthedocs.io/en/stable/guide/rest_framework.html#drf-integration

https://django-filter.readthedocs.io/en/stable/ref/filterset.html

https://www.geeksforgeeks.org/customizing-filters-in-django-rest-framework/

https://www.django-rest-framework.org/api-guide/filtering/

przy czym pamietac by w view dodac zarowno filter backend jak i filterset_class (wazne set, a nie tylko filter)

# uzyskiwanie danych z axios i composables

mogloby sie wydawac ze wystarczy podazac za https://vuejs.org/guide/reusability/composables.html, ktore prezentuje wlasnie takie wykorzystanie, tylko ze z fetchem

problemami jest jednak ze:
- przy zwracaniu nie czeka to az dane zostana pobrane - w rezultacie komponent wykorzystujacy composable dostaje puste wartosci, a ja bym chcial wykorzystac tylko kiedy juz beda wlasciwe
- niemozliwe jest w js (albo ja nie potrafie) zwrocenie destructuring assignment z funkcji zwracajacej obiekt do istniejacych juz zmiennych, wszedzie pokazane jest przypisanie do nowych, wobec czego dla dzialania wywolanie funkcji zostalo owiniete w await oraz przypsisanie wartosci do nowych tymczasowych zmiennych, a nastepnie dopiero do wlasciwych

tzn. np dla zwracania z paginacja
composable:
```
import {ref, toValue} from 'vue';
import axios from 'axios';

export async function useAxiosGetPaginated(url){
    const data = ref();
    const pages = ref();
    const error = ref();

    const response = await axios.get(toValue(url))
    .then((res)=>{
        data.value = res.data.results;
        pages.value = res.data.context.page_links;
    })
    .catch((err)=>{
        console.log(err);
        error.value = err;
    })
    return {data, pages, error}
}
```

odbior danych: 
```
import { useAxiosGetPaginated } from '../../composables/useAxiosGetPaginated';

const reviews = ref();
const pages = ref();
const error = ref();

const url = ref(`api/reviews/?product=${product.value.slug}`);

const getReviews = async (link) => {
    const {data, pages, error} = await useAxiosGetPaginated(link);
    reviews.value = data.value;
    pages.value = pages.value;
    if (error) error.value = error.value;
}

getReviews(url.value);
```

#### problemy
**UWAGA:** dla odbierania danych z paginacja, jesli zwracasz obiekt o nazwie np. pages, to odbierajac, uwazaj, by przypisywac go ostatecznie do obiektu o innej nazwie, bo moze sie mylic, nie wiedziec co do czego przypisywac i konczysz z pustymi zawsze obiektami mimo ze odbiera dane poprawnie

# Zwracanie custom exceptions, kiedy zwracanie zwyklych respoonse z status 400 nie dziala

nie wiem czemu nie dziala, nie rozumie tego front jako error tylko jako zwykly sukces response, ale mozna albo zamiast zwracania zrobic raise APIException (co tez zwraca Response internally)

albo stworzyl wlasny exception handler rozszerzajac bazowy:
https://medium.com/turkcell/request-validation-and-custom-exception-handling-in-django-rest-framework-649fddecb415


# Formatowanie dat tylko z js
https://www.freecodecamp.org/news/how-to-format-dates-in-javascript/
tzn konwersja otrzymanego obiektu z db na new Date() i nastepnie metody konwersji z Date do string wbudowane

# kwestia dark theme
jakos dziwnie dziala ten toolbar - jakby nie byl aktualizowny plik kompletnie
ale anyways:

sposoby znalezione:

utworzenie dwoch zestawow css zmiennych, ktorych wartosci beda zmieniane, tzn zmiana miedzy dwoma zestawami w root albo body, wtedy wszystkie kolory elementow w wszystkich plikach musza byc zwiazane z tymi zmiennymi

sprobowalem:
- https://dev.to/ananyaneogi/create-a-dark-light-mode-switch-with-css-variables-34l8

czyli z 

document.documentElement.setAttribute('data-theme', 'dark'); ustawianym na switchu - luja

- https://css-tricks.com/a-complete-guide-to-dark-mode-on-the-web/#aa-using-custom-properties
czyli ze zmienianem klasy na body i wlasnie w body przechowywaniu zmiennych - luja

- https://mwichary.medium.com/dark-theme-in-a-day-3518dde2955a
podobny sposob tylko po elemencie html zamiast :root - tez chuja...

- dopiero co zadzialalo:
https://dev.to/tqbit/create-your-own-dark-mode-toggle-component-with-vue-js-1284

czyli ustawianie jednych zmiennych na :root
a drugich na :root.dark
i zmienianie klasy

ale dopiero zadzialo kiedy dodales tez klase .light

i w podstawowej klasie byly domyslne elementy

# integerfield z choices

normalnie jest to mozliwe to zrobienia, ale gdybys pozniej chcial recznie to przypisywac, to musialbys ustawiac wartosc pola po liczbach, a nie human readable (human readble jest tylko dla stron), ale mozna to zalatwic przypisujac wartosic do zmiennych a potem te zmienne umiescic w zbierze wyborow, see:
https://stackoverflow.com/questions/1117564/set-django-integerfield-by-choices-name


# Uzywanie custom permissions w Django views, zarowno function jak i class based, np. jedynie autor moze modyfikowac obiekt

wiecej informacji:

https://docs.djangoproject.com/en/3.1/topics/auth/default/#django.contrib.auth.mixins.UserPassesTestMixin

generalnie za pomoca funkcji do FBV lub mixinow do CBV mozna tworzyc funkcje ktore beda sprawdzac customowy warunek typu czy request.user zgadza sie z polem author na obiekcie i inne, samo zwroci exception PermissionDenied / 403 Forbidden response
latwo mieszalne z login_required lub mixinem LoginRequiredMixin

# zapisywanie informacji w modelu zaleznych od informacji z innego related

bardzo wygodnie jest robic to w metodach save modeli np. dla zamowienia Order

```
def save(self, *args, **kwargs):
    self.sum_items = self.items.count()
    self.shipping_cost = self.shipping_method.price
    cost = 0
    for item in self.items.all():
        cost += item.product.price_discounted
    self.sum_cost = cost/self.sum_items
    self.sum_cost = self.sum_cost * (1-self.discount)
    if self.sum_cost < 250:
        self.sum_cost += self.shipping_cost
    return super().save(*args, **kwargs)
```

wykorzystuje ono bez problemu pola z powiazanych modeli, gdzie powiazanie jest w przypadku np items sprecyzowane na innym modelu! (CartItem w tym wypadku), a price_discounted jest funkcja otoczona @property, dzieki czemu mozemy korzystac z niej jak field value

a potem np. w views wykonywac metody .save() wszystkich modeli do ktorych doszlo powiazanie itd i powinno dzialac super

zamiast bawic sie robienie tego recznie w kazdym view


# kolejnosc urlpatterns
Troche specyficznie dla tego projektu, gdyz oczekuje, ze Vue Router bedzie przechwytywalo roznego rodzaju sciezki

dlatego urls dla vue zaczynaja sie od '', czyli lapia wszystko

dlatego aby cokolwiek innego dzialalo, trzeba umieszczac jego urls przed tym catch-allem


# generowanie uml diagrams z modeli:

https://django-extensions.readthedocs.io/en/latest/graph_models.html

oraz zainstalowanie graphviz na komputerze i dodanie bin do PATH


============================================================


# drf put/patch generic views debugging template

```
    # debugging template:

    # def put(self, request, *args, **kwargs):
    #     print('update request data: ', self.request.data)
    #     return self.update(request, *args, **kwargs)

    # def patch(self, request, *args, **kwargs):
    #     print('update request data: ', self.request.data)
    #     return self.partial_update(request, *args, **kwargs)
    
    # def update(self, request, *args, **kwargs):
    #     partial = kwargs.pop('partial', False)
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #     # serializer.is_valid(raise_exception=True)
    #     if serializer.is_valid():
    #         self.perform_update(serializer)
    #     else:
    #         print('serializer.errors: ', serializer.errors)

    #     if getattr(instance, '_prefetched_objects_cache', None):
    #         # If 'prefetch_related' has been applied to a queryset, we need to
    #         # forcibly invalidate the prefetch cache on the instance.
    #         instance._prefetched_objects_cache = {}

    #     return Response(serializer.data)

    # def perform_update(self, serializer):
    #     serializer.save()

    # def partial_update(self, request, *args, **kwargs):
    #     kwargs['partial'] = True
    #     return self.update(request, *args, **kwargs)
    
```

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