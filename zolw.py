from zwierze import Zwierze
import random

class Zolw(Zwierze):

    def __init__(self, mapa, x, y):
        super(Zolw, self).__init__(5, (215, 252, 0), 2, 1, x, y, mapa)

    def __str__(self):
        return 'zolw'

    def czyOdbilAtak(self, x2, y2):
        org = self._mapa[x2][y2]
        if org.getSila()<5:
            return 1
        else:
            return 0

    def akcja(self):
        if random.randint(0, 3) == 0:
            super(Zolw, self).akcja()

    def _rozmnazaj(self, a, b):
        Zolw(self._mapa, a, b)
