# ukonczone cele konkretne rozpisane

plik stworzony pozno

- realizacja funkcji favorites:
[x] - dodanie do modelu uzytkownika relacji z ulubionymi produktami
[x] - API obsluga dodawania produktu do ulubionych uzytkownika, np. products/slug/favourite, z przekazywaniem nazwy uzytkownika
[x] - obsluga dodawania do favorites z poziomu strony produktu w vue\
[x] - dynamiczne wyswietlanie store product grid
[x] - funkcja dodawania do favorites w gridzie

- koszyk:
[x] ProductRight - funkcjonalnosci dodawania do koszyka, favorites, przechodzenia do koszyka:
[x] endpoint dodawania produktu do koszyka
[x] dodawanie do koszyka z strony produktu
[x] dodawanie do koszyka z strony gridu
[x] endpoint usuwania z koszyka
[x] dynamiczna strona koszyka
[x] usuwanie z koszyka z poziomu strony koszyka
[x] koszyk jest zwiazany z produktami i uzytkownikiem, wiec kwestia przekazywania i aktualizacji w navie - moze dodac store na koszyk, zeby mogl byc aktualizowany z dowolnego miejsca
[x] proby takiej wlasnie synchronizacji aktualizacji
[x] zwiekszanie ilosci przedmiotow danego typu w z poziomu strony koszyka
[x] z poziomu strony koszyka - jesli kliniemy dwukrotnie "dodaj do koszyka" to powinno dodac drugi raz itd?
[x] dynamicznosc strony koszyka wlacznie z czy przedmioty w ulubionych?

- realizacja poprzez API dodawania produktow do koszyka:
[x] endpointy - cart zwiazany jest z uzytkownikiem, wiec w endpoincie sproboj wykorzystac request user a potem jego cart, a w tresci sprobuj przekazywac obiekt produktu (ale nie wiem czy mozliwe bo serializacja usera), a jak nie to po slugu
[x] obluga na stronie produktu
[x] dodac jakos do grid
[x] na sklepie produktu przycisk "buy now" zeby dodawal do cartu i przechodzil do strony koszyka
[x] odbieranie danych o koszyku w navie - a moze jako czesc serializatora uzytkownika po prostu? ale wtedy koszyk musialby tez zawierac produkty itd, ale to ok, bo to jego integralna czesc
[x] odbieranie danych na stronie koszyka
[x] usuwanie z koszyka z poziomu strony koszyka - jesli jest wiele takich samych to jak precyzowac ktory usuwac itd..
[x] tak samo zmienianie ilosci w koszyku - jak precyzowac
[x] ogolnie zmienianie ilosci - najprosciej 1 przyciskiem typu +1, ale gdyby selectem, to by trzeba przekazywac ten numer i jaki produkt dodac
[x] Na start wyswietlanie po prostu wszystkich jak leci, ale potem jesli ten sam produkt to niech Vue scala w jedno tylko z numerkiem