from zwierze import Zwierze

class Wilk(Zwierze):

    def __init__(self, mapa, x, y):
        super(Wilk, self).__init__(6, (105, 105, 105), 9, 5, x, y, mapa)

    def __str__(self):
        return 'wilk'

    def _rozmnazaj(self, a, b):
        Wilk(self._mapa, a, b)