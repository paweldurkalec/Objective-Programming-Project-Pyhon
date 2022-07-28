import abc

class Organizm():
    __metaclass__ = abc.ABCMeta

    def __init__(self, kolor, sila, inicjatywa, x, y, mapa):
        self._xSwiata = len(mapa)
        self._ySwiata = len(mapa[0])
        self._wiek = 0
        self._kolor = kolor
        self._sila = sila
        self._inicjatywa = inicjatywa
        self._x = x
        self._y = y
        self._mapa = mapa
        self._mapa[x][y] = self
        self._listaZdarzen = []

    def umiescZdarzeniaWDzienniku(self, dziennik):
        for element in self._listaZdarzen:
            dziennik.dodajWydarzenie(element)

        self._listaZdarzen = []

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def getColour(self):
        return self._kolor

    def getSila(self):
        return self._sila

    def getInit(self):
        return self._inicjatywa

    def getWiek(self):
        return self._wiek

    def setX(self, newX):
        self._x = newX

    def setY(self, newY):
        self._y = newY

    def setWiek(self, newWiek):
        self._wiek = newWiek

    def setSila(self, ile):
        self._sila = ile

    def dajSile(self, ile):
        self._sila += ile

    def zapisz(self, file):
        file.write(str(self) + ' ' + str(self._x) + ' ' + str(self._y) + ' ' + str(self._sila) + ' ' + str(self._wiek) + '\n')

    def _czyGdziekolwiekWolne(self):
        if self._y > 0:
            if self._mapa[self._x][self._y-1] == 0:
                return 1
        if self._x < self._xSwiata - 1:
            if self._mapa[self._x + 1][self._y] == 0:
                return 1
        if self._y < self._ySwiata - 1:
            if self._mapa[self._x][self._y + 1] == 0:
                return 1
        if self._x > 0:
            if self._mapa[self._x - 1][self._y] == 0:
                return 1
        return 0

    def _czyWolne(self, kierunek):
        if kierunek == 0:
            if self._y > 0:
                if self._mapa[self._x][self._y - 1] == 0:
                    return 1
                else:
                    return 2
        elif kierunek == 1:
            if self._x < self._xSwiata - 1:
                if self._mapa[self._x + 1][self._y] == 0:
                    return 1
                else:
                    return 2
        elif kierunek == 2:
            if self._y < self._ySwiata - 1:
                if self._mapa[self._x][self._y + 1] == 0:
                    return 1
                else:
                    return 2
        elif kierunek == 3:
            if self._x > 0:
                if self._mapa[self._x - 1][self._y] == 0:
                    return 1
                else:
                    return 2
        return 0
