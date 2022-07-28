from zwierze import Zwierze
import random

class Antylopa(Zwierze):

    def __init__(self, mapa, x, y):
        super(Antylopa, self).__init__(5, (139, 69, 19), 4, 4, x, y, mapa)

    def __str__(self):
        return 'antylopa'

    def czyUcieka(self):
        if random.randint(0, 1) == 0 and self._czyGdziekolwiekWolne():
            self.__uciekaj()
            return 1
        return 0

    # nie wywoluje metody akcja z klasy zwierze poniewaz wykonuje ruchy o 2 pola, a nie o jedno
    def akcja(self):
        nextX = self._x
        nextY = self._y
        kierunek = random.randint(0, 3)
        if kierunek == 0:
            nextY -= 2
        elif kierunek == 1:
            nextX += 2
        elif kierunek == 2:
            nextY += 2
        elif kierunek == 3:
            nextX -= 2
        rodzajAkcji = self._czyWolne(kierunek)
        if rodzajAkcji == 0:
            self.akcja()
        elif rodzajAkcji == 1:
            self._mapa[self._x][self._y] = 0
            self._x = nextX
            self._y = nextY
            self._wiek += 1
            self._zwiekszCzasOdOstRozmn()
            self._rysowanie()
        elif rodzajAkcji == 2:
            self._kolizja(nextX, nextY)
            self._wiek += 1
            self._zwiekszCzasOdOstRozmn()

    def _rozmnazaj(self, a, b):
        Antylopa(self._mapa, a, b)

    def _czyGdziekolwiekWolne(self):
        if self._y > 1:
            if self._mapa[self._x][self._y-2] == 0:
                return 1
        if self._x < self._xSwiata - 2:
            if self._mapa[self._x + 2][self._y] == 0:
                return 1
        if self._y < self._ySwiata - 2:
            if self._mapa[self._x][self._y + 2] == 0:
                return 1
        if self._x > 1:
            if self._mapa[self._x - 2][self._y] == 0:
                return 1
        return 0

    def _czyWolne(self, kierunek):
        if kierunek == 0:
            if self._y > 1:
                if self._mapa[self._x][self._y - 2] == 0:
                    return 1
                else:
                    return 2
        elif kierunek == 1:
            if self._x < self._xSwiata - 2:
                if self._mapa[self._x + 2][self._y] == 0:
                    return 1
                else:
                    return 2
        elif kierunek == 2:
            if self._y < self._ySwiata - 2:
                if self._mapa[self._x][self._y + 2] == 0:
                    return 1
                else:
                    return 2
        elif kierunek == 3:
            if self._x > 1:
                if self._mapa[self._x - 2][self._y] == 0:
                    return 1
                else:
                    return 2
        return 0

    def _kolizja(self, x2, y2):
        org = self._mapa[x2][y2]
        if org.czyZwierze() and not isinstance(org, Antylopa) and random.randint(0, 1) == 0:
            tempX = self._x
            tempY = self._y
            self._x = x2
            self._y = y2
            if self._czyGdziekolwiekWolne():
                self.__uciekaj(tempX, tempY)
            else:
                self._x = tempX
                self._y = tempY
        else:
            super(Antylopa, self)._kolizja(x2, y2)

    def __uciekaj(self, tempX=-1, tempY=-1):
        kierunek = random.randint(0, 3)
        nextX = self._x
        nextY = self._y
        while not self._czyWolne(kierunek) == 1:
            kierunek = random.randint(0, 3)
        if kierunek == 0:
            nextY -= 2
        elif kierunek == 1:
            nextX += 2
        elif kierunek == 2:
            nextY += 2
        elif kierunek == 3:
            nextX -= 2
        if tempX != -1:
            self._mapa[tempX][tempY] = 0
        else:
            self._mapa[self._x][self._y] = 0
        self._x = nextX
        self._y = nextY
        self._listaZdarzen.append(
            str(self) + ' ucieka przed walka na (' + str(self.getX()) + ',' + str(self.getY()) + ')')
        self._rysowanie()