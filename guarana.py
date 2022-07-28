from roslina import Roslina

class Guarana(Roslina):
    def __init__(self, mapa, x, y):
        super(Guarana, self).__init__((127, 0, 255), 0, x, y, mapa)
        self._rozmnazanie = 15

    def __str__(self):
        return 'guarana'

    def czyDajeSile(self, org):
        self._kolizja(org.getX(), org.getY())
        return 1

    def _rozmnazaj(self, a, b):
        Guarana(self._mapa, a, b)

    def _kolizja(self, x2, y2):
        org = self._mapa[x2][y2]
        org.dajSile(3)