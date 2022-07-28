from organizm import Organizm
import abc
import random

class Roslina(Organizm):
    __metaclass__ = abc.ABCMeta

    def __init__(self, kolor, sila, x, y, mapa):
        super(Roslina, self).__init__(kolor, sila, 0, x, y, mapa)
        self._rozmnazanie = 10

    def czyTruje(self, org):
        return False

    def czyDajeSile(self, org):
        return False

    def czyOdbilAtak(self, x2, y2):
        return 0

    def czyUcieka(self):
        return False

    def czyZwierze(self):
        return False

    def akcja(self):
        czyRozmnazac = random.randint(0, self._rozmnazanie-1)
        if czyRozmnazac==0 and self._czyGdziekolwiekWolne():
            kierunek = random.randint(0, 3)
            newX = self._x
            newY = self._y
            while not super()._czyWolne(kierunek) == 1:
                kierunek = random.randint(0, 3)
            if kierunek == 0:
                newY -= 1
            elif kierunek == 1:
                newX += 1
            elif kierunek == 2:
                newY += 1
            elif kierunek == 3:
                newX -= 1
            self._rozmnazaj(newX, newY)
            self._listaZdarzen.append(str(self) + ' rozprzestrzenia sie na (' + str(newX) + ',' + str(newY) + ')')
        self._wiek+=1
        self._rysowanie()

    def _rysowanie(self):
        self._mapa[self._x][self._y] = self

    def _kolizja(self, x, y):
        return

    def _rozmnazaj(self, a, b):
        print('error')
        return




