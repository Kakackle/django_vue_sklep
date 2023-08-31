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


