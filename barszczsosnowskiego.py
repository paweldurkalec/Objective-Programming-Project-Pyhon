from roslina import Roslina
import cyberowca

class BarszczSosnowskiego(Roslina):
    def __init__(self, mapa, x, y):
        super(BarszczSosnowskiego, self).__init__((153, 51, 102), 0, x, y, mapa)
        self._rozmnazanie = 20

    def __str__(self):
        return 'barszcz_sosnowskiego'

    def czyTruje(self, org):
        if org.czyZwierze() and not isinstance(org, cyberowca.CyberOwca):
            self._kolizja(org.getX(), org.getY())
            return 1
        return 0

    def akcja(self):
        self.__eksterminujSasiedztwo()
        super(BarszczSosnowskiego, self).akcja()

    def _rozmnazaj(self, a, b):
        BarszczSosnowskiego(self._mapa, a, b)

    def _kolizja(self, x2, y2):
        self._mapa[x2][y2] = 0
        self._mapa[self._x][self._y] = 0

    def __eksterminujSasiedztwo(self):
        org = 0
        if self._y > 0:
            org = self._mapa[self._x][self._y-1]
            if org != 0:
                if org.czyZwierze() and not isinstance(org, cyberowca.CyberOwca):
                    self._mapa[org.getX()][org.getY()] = 0
                    self._listaZdarzen.append(
                        str(org) + ' zostal spalony przez BS na (' + str(org.getX()) + ',' + str(org.getY()) + ')')
        if self._x < self._xSwiata - 1:
            org = self._mapa[self._x + 1][self._y]
            if org != 0:
                if org.czyZwierze() and not isinstance(org, cyberowca.CyberOwca):
                    self._mapa[org.getX()][org.getY()] = 0
                    self._listaZdarzen.append(
                        str(org) + ' zostal spalony przez BS na (' + str(org.getX()) + ',' + str(org.getY()) + ')')
        if self._y < self._ySwiata - 1:
            org = self._mapa[self._x][self._y + 1]
            if org != 0:
                if org.czyZwierze() and not isinstance(org, cyberowca.CyberOwca):
                    self._mapa[org.getX()][org.getY()] = 0
                    self._listaZdarzen.append(
                        str(org) + ' zostal spalony przez BS na (' + str(org.getX()) + ',' + str(org.getY()) + ')')
        if self._x > 0:
            org = self._mapa[self._x - 1][self._y - 1]
            if org != 0:
                if org.czyZwierze() and not isinstance(org, cyberowca.CyberOwca):
                    self._mapa[org.getX()][org.getY()] = 0
                    self._listaZdarzen.append(
                        str(org) + ' zostal spalony przez BS na (' + str(org.getX()) + ',' + str(org.getY()) + ')')