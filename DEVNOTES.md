# Devnotes

## Obsluga path do vue i reszty w Django

Potencjalnie porzadane jest aby path do aplikacji Vue byl explicit, np /vue albo /sklep jesli projekt jest sklepem itd
Chociaz byc moze jest to nie do konca intuicyjne dla uzytkownika

ale, jesli chcemy miec konkretny poczatek sciezki, router musi to rozpoznawac

Aby mogl to robic, nalezy dac mu o tym znac

Majac vue.config.js mozna ustawic tam: https://stackoverflow.com/questions/66284893/how-do-you-control-your-publicpath-property-in-vue-config-js

jesli nie mozna podac w createWebHistory('/path')