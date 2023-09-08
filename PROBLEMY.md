# nie dziala permissions

konkretnie, w napisanym IsOwnerOrReadOnly

nawet jesli manualnie w view wywolujemy check_object_permission to zwyczajnie przy patchu nigdy tam nie wchodzi (bo nigdy nie wywoluje printa przy patch, przy get juz tak)

i nie ma to sensu

jedna kwestia - jesli chcesz sprawdzac has_object_permission, musisz sprawdzac has_permission - to okej

ale potem nie dziala

linki:
https://testdriven.io/blog/custom-permission-classes-drf/

https://stackoverflow.com/questions/66739195/django-rest-framework-custom-permission-not-working

https://prithoo11335.medium.com/custom-permission-classes-in-django-restframework-6dc1d26bba33

https://stackoverflow.com/questions/38718454/django-rest-framework-owner-permissions

https://stackoverflow.com/questions/62274490/has-object-permission-not-called-from-put-or-patch-request

i poki co nie dziala i chuj, wylaczam

zrobie to jak bede chcial sam w metodzie patch sprawdzanie czy autor sie zgadza, bo kurwa

tak to jest jak chcesz sie wyreczac czyms automatycznym