# TODO: Optional todos etc

## Conditional product forms / rozdzielenie na rozne typy produktow

Gdybysmy chcieli uzyskac dokladniejsze informacje o produktach, a majac wiele typow produktow, moglibysmy np:

1. Stworzyc podstawowy typ Produkt z cena, powiazaniem z uzytkownikiem, manufacturer itd i nastepnie wykorzystujac inheritance stworzyc kolejne modele typu EffectProduct z polami stosownymi dla efektu, GuitarProduct z wlasnymi innymi polami itd

2. Wykorzystac zewnetrzna biblioteke, cos jak:
https://django-formset.readthedocs.io/en/latest/intro.html

ktore ma nieco inna skladnie od zwyklych Django Form, ale umozliwia deklarowac warunki renderowania pol, dokonuje weryfikacji bez reloadu itd

3. Zrobic to co biblioteka ale recznie, z reloadem typu:
https://www.fusionbox.com/blog/detail/creating-conditionally-required-fields-in-django-forms/577/

tzn. po pierwotnym przeslaniu sprawdzajac w form validation czy jakies pole jest ustawione i jesli tak, to zwracac forme z nowymi polami

4. Recznie z javascriptem, przy czym trzeba by wyodrebnic pole z form

5. costam multiple forms https://stackoverflow.com/questions/1483647/django-model-form-include-fields-from-related-models

**POKI CO: wszystko w jednym modelu, ale pola nie pasujace do kazdego produktu sa opcjonalne**

przy czym, aby latwiej renderowac, mozna by przy przyjmowaniu form jesli typ nie zgadza sie z jakims, to pola nie pasujace wynullowac