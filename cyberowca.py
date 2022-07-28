from zwierze import Zwierze
import barszczsosnowskiego
import random

class CyberOwca(Zwierze):

    def __init__(self, mapa, x, y):
        super(CyberOwca, self).__init__(6, (0, 0, 255), 11, 5, x, y, mapa)

    def __str__(self):
        return 'cyber-owca'

    def akcja(self):
        if self.__czyNaMapieJestBarszcz():
            self.__eksterminujBarszcz()
        else:
            super(CyberOwca, self).akcja()

    def _rozmnazaj(self, a, b):
        CyberOwca(self._mapa, a, b)

    def __czyNaMapieJestBarszcz(self):
        for i in range(0, self._xSwiata):
            for j in range(0, self._ySwiata):
                if isinstance(self._mapa[i][j], barszczsosnowskiego.BarszczSosnowskiego):
                    return 1
        return 0

    def __odleglosc(self, organizm):
        return abs(organizm.getX() - self._x) + abs(organizm.getY() - self._y)

    def __znajdzNajblizszyBarsz(self):
        tablicaBarszczy = []
        for i in range(0, self._xSwiata):
            for j in range(0, self._ySwiata):
                if isinstance(self._mapa[i][j], barszczsosnowskiego.BarszczSosnowskiego):
                    tablicaBarszczy.append(self._mapa[i][j])
        minOdl = self._xSwiata + self._ySwiata + 1
        koordynaty = [0, 0]

        for barszcz in tablicaBarszczy:
            odlOdAkt = self.__odleglosc(barszcz)
            if  odlOdAkt < minOdl:
                koordynaty[0] = barszcz.getX()
                koordynaty[1] = barszcz.getY()
                minOdl = odlOdAkt

        return koordynaty

    def __eksterminujBarszcz(self):
        koordynaty = self.__znajdzNajblizszyBarsz()
        if koordynaty[0] != self._x and koordynaty[1] != self._y:
            if random.randint(0, 1) == 0:
                moveDir = 0
            else:
                moveDir = 1
        elif koordynaty[0] != self._x:
            moveDir = 0
        else:
            moveDir = 1

        if moveDir == 0:
            if self._x < koordynaty[0]:
                nextX = self._x + 1
                nextY = self._y
                kierunek = 1
            else:
                nextX = self._x - 1
                nextY = self._y
                kierunek = 3
        else:
            if self._y < koordynaty[1]:
                nextX = self._x
                nextY = self._y + 1
                kierunek = 2
            else:
                nextX = self._x
                nextY = self._y - 1
                kierunek = 0

        rodzajAkcji = self._czyWolne(kierunek)
        if rodzajAkcji == 0:
            print('error')
            pass
        elif rodzajAkcji == 1:
            self._mapa[self._x][self._y] = 0
            self._x = nextX
            self._y = nextY
            self._wiek += 1
            self.zwiekszCzasOdOstatniegoRozmnazania()
            self._rysowanie()
        elif rodzajAkcji == 2:
            self._kolizja(nextX, nextY)
            self._wiek += 1
            self.zwiekszCzasOdOstatniegoRozmnazania()












