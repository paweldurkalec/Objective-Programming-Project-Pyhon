from roslina import Roslina

class Trawa(Roslina):
    def __init__(self, mapa, x, y):
        super(Trawa, self).__init__((0, 154, 23), 0, x, y, mapa)

    def __str__(self):
        return 'trawa'

    def _rozmnazaj(self, a, b):
        Trawa(self._mapa, a, b)
