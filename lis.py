from zwierze import Zwierze

class Lis(Zwierze):

    def __init__(self, mapa, x, y):
        super(Lis, self).__init__(5, (255, 131, 0), 3, 7, x, y, mapa)

    def __str__(self):
        return 'lis'

    def akcja(self):
        if self._czyGdziekolwiekWolne():
            super(Lis, self).akcja()

    def _rozmnazaj(self, a, b):
        Lis(self._mapa, a, b)

    def _czyGdziekolwiekWolne(self):
        if self._y > 0:
            if self._mapa[self._x][self._y-1] == 0:
                return 1
            elif self._mapa[self._x][self._y-1].getSila() <= self.getSila():
                return 1
        if self._x < self._xSwiata - 1:
            if self._mapa[self._x + 1][self._y] == 0:
                return 1
            elif self._mapa[self._x + 1][self._y].getSila() <= self.getSila():
                return 1
        if self._y < self._ySwiata - 1:
            if self._mapa[self._x][self._y + 1] == 0:
                return 1
            elif self._mapa[self._x][self._y + 1].getSila() <= self.getSila():
                return 1
        if self._x > 0:
            if self._mapa[self._x - 1][self._y] == 0:
                return 1
            elif self._mapa[self._x - 1][self._y].getSila() <= self.getSila():
                return 1
        return 0

    def _czyWolne(self, kierunek):
        if kierunek == 0:
            if self._y > 0:
                if self._mapa[self._x][self._y - 1] == 0:
                    return 1
                elif self._mapa[self._x][self._y - 1].getSila() > self.getSila():
                    return 0
                else:
                    return 2
        elif kierunek == 1:
            if self._x < self._xSwiata - 1:
                if self._mapa[self._x + 1][self._y] == 0:
                    return 1
                elif self._mapa[self._x + 1][self._y].getSila() > self.getSila():
                    return 0
                else:
                    return 2
        elif kierunek == 2:
            if self._y < self._ySwiata - 1:
                if self._mapa[self._x][self._y + 1] == 0:
                    return 1
                elif self._mapa[self._x][self._y + 1].getSila() > self.getSila():
                    return 0
                else:
                    return 2
        elif kierunek == 3:
            if self._x > 0:
                if self._mapa[self._x - 1][self._y] == 0:
                    return 1
                elif self._mapa[self._x - 1][self._y].getSila() > self.getSila():
                    return 0
                else:
                    return 2
        return 0