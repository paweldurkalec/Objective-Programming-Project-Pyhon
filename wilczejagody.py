from roslina import Roslina

class WilczeJagody(Roslina):
    def __init__(self, mapa, x, y):
        super(WilczeJagody, self).__init__((255, 40, 0), 0, x, y, mapa)
        self._rozmnazanie = 15

    def __str__(self):
        return 'wilcze_jagody'

    def czyTruje(self, org):
        if org.czyZwierze():
            self._kolizja(org.getX(), org.getY())
            return 1
        return 0

    def _rozmnazaj(self, a, b):
        WilczeJagody(self._mapa, a, b)

    def _kolizja(self, x2, y2):
        self._mapa[x2][y2] = 0
        self._mapa[self._x][self._y] = 0
