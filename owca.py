from zwierze import Zwierze

class Owca(Zwierze):

    def __init__(self, mapa, x, y):
        super(Owca, self).__init__(4, (255, 250, 250), 4, 4, x, y, mapa)

    def __str__(self):
        return 'owca'

    def _rozmnazaj(self, a, b):
        Owca(self._mapa, a, b)


