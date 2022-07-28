from roslina import Roslina

class Mlecz(Roslina):
    def __init__(self, mapa, x, y):
        super(Mlecz, self).__init__((249, 215, 28), 0, x, y, mapa)

    def __str__(self):
        return 'mlecz'

    def akcja(self):
        for i in range(3):
            super(Mlecz, self).akcja()

    def _rozmnazaj(self, a, b):
        Mlecz(self._mapa, a, b)