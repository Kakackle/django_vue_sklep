# Django + Vue w jednym projekcie
Z wykorzystaniem webpacku, babel, vue-loader

Django serwuje statyczne pliki Vue

Django obsluguje modele i udostepnia przez REST API z DRF do Vue na tym samym porcie

Vue obsluguje wiekszosc funkcjonalnosci, obsluge url z pomoca Vue Router itd

## Cel: strona sklepu z efektami gitarowymi?

Chyba tak, poki co sa tylko bardzo przykladowe modele i view ale generalnie wszystko wydaje sie realne

w tym realizacja np. osobnych view ktore nie beda wykorzystywaly Vue a tylko Django by wykorzystac moc Django forms itp

## Glownie zrealizowane z wykorzystaniem:

https://www.saaspegasus.com/guides/modern-javascript-for-django-developers/integrating-django-react/

oraz:

https://vue-loader.vuejs.org/guide/



### pomocne takze:

https://www.webucator.com/article/connecting-django-and-vue/


## Alternatywy:

https://codewithstein.com/combining-django-and-vuejs-everything-you-need-to-know/ 

z czego czesto spotykane django-webpack loader, majace zalatwiac webpack za nas, zamiast pisac wlasny config

jak tu:
https://onlinecode.org/building-modern-applications-with-django-vue-js-and-auth0-part-2/


### NGINX:

https://www.reddit.com/r/django/comments/maykzc/how_to_run_django_and_vue_or_any_spa_on_the_same/

tez brzmi jak ciekawa, wartosciowa opcja, nginx serwuje oba, laczy traffic miedzy nimi

https://stackoverflow.com/questions/60705957/django-react-how-to-connect-them-for-deployment/60706686#60706686


## do przejscia: 

https://auth0.com/blog/building-modern-applications-with-django-and-vuejs/

https://dafoster.net/articles/2021/02/16/building-web-apps-with-vue-and-django-the-ultimate-guide/

https://testdriven.io/blog/django-spa-auth/
