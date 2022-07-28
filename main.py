"""
Sterowanie:
    q, przycisk "Nastepna tura" - nastepna tura
    strzalki - zmiana kierunku czlowieka
    scroll myszy - przewijanie listy wydarzen
    w - aktywacja tarczy Alzura
    s - zapisanie rozgrywki
    r - wczytanie rozgrywki
    esc - wyjscie
    przyciski z nazwami organizmow - pozwalaja wybrac organizm, ktory zostanie dodany na mape po nacisnieciu
        na wolne pole
Miejsce zapisu/odczytu:
    zapis.txt
Plik konfiguracyjny:
    config.txt
Organizmy:
    Przypisanie organizmow do kolorow wystwietla sie nad mapa podczas gry
Organizmy rozmieszczane losowo(czlowiek(X/2,Y/2)), ilosc organizmow (wraz z czlowiekiem) na poczatku nie moze byc wieksza
    niz ilosc dostepnych pol (X*Y), w innym wypadku symulacja sie nie uruchomi
"""
from swiat import Swiat

swiat = Swiat()
while not swiat.getExit():
    swiat.wykonajTure()