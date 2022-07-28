from zwierze import Zwierze
import random

class Czlowiek(Zwierze):

    def  __init__(self, mapa, x = -1, y = -1, kierunek = 0, tarczaAlzura = 0, licznikTarczy = 0, cooldownTarczy = 0):
        if x == -1:
            x = int(len(mapa)/2)
            y = int(len(mapa[0])/2)

        super(Czlowiek, self).__init__(0, (0, 255, 255), 5, 4, x, y, mapa)
        self.__kierunek = kierunek
        self.__tarczaAlzura = tarczaAlzura
        self.__licznikTarczy = licznikTarczy
        self.__cooldownTarczy = cooldownTarczy

    def __str__(self):
        return 'czlowiek'

    def umiescZdarzeniaWDzienniku(self, dziennik):
        for element in self._listaZdarzen:
            dziennik.dodajWydarzenieNaPoczatek(element)

        self._listaZdarzen = []

    def czyOdbilAtak(self, x2, y2):
        if self.__tarczaAlzura:
            return 2
        else:
            return 0

    def setKierunek(self, newK):
        self.__kierunek = newK

    def setTarcza(self, t):
        self.__tarczaAlzura = t

    def getTarcza(self):
        return self.__tarczaAlzura

    def getCooldownTarczy(self):
        return self.__cooldownTarczy

    def resetLicznikTarczy(self):
        self.__licznikTarczy = 0

    def getKierunek(self):
        return self.__kierunek

    def zapisz(self, file):
        file.write(str(self) + ' ' + str(self._x) + ' ' + str(self._y) + ' ' + str(self._sila) + ' ' + str(self._wiek) +
                   ' ' + str(self.__kierunek) + ' ' + str(self.__tarczaAlzura) + ' ' + str(self.__licznikTarczy) + ' ' + str(self.__cooldownTarczy) + '\n')

    def akcja(self):
        nextX = self._x
        nextY = self._y
        if self.__kierunek == 0:
            nextY -= 1
        elif self.__kierunek == 1:
            nextX += 1
        elif self.__kierunek == 2:
            nextY += 1
        elif self.__kierunek == 3:
            nextX -= 1

        rodzajAkcji = self._czyWolne(self.__kierunek)
        if rodzajAkcji == 1:
            self._mapa[self._x][self._y] = 0
            self._x = nextX
            self._y = nextY
            self._rysowanie()
        elif rodzajAkcji == 2:
            self._kolizja(nextX, nextY)
        self._wiek += 1
        self.__obsluzTarczeAlzura()

    def _kolizja(self, x2, y2):
        org = self._mapa[x2][y2]
        if org.czyZwierze() and self.czyOdbilAtak(x2, y2) == 2:
            tempX = self._x
            tempY = self._y
            self._x = x2
            self._y = y2
            if self._czyGdziekolwiekWolne():
                kierunek = random.randint(0, 3)
                nextX = self._x
                nextY = self._y
                while not self._czyWolne(kierunek) == 1:
                    kierunek = random.randint(0, 3)
                if kierunek == 0:
                    nextY -= 1
                elif kierunek == 1:
                    nextX += 1
                elif kierunek == 2:
                    nextY += 1
                elif kierunek == 3:
                    nextX -= 1
                self._rysowanie()
                self._mapa[tempX][tempY] = 0
                self._mapa[nextX][nextY] = org
                org.setX(nextX)
                org.setY(nextY)
            else:
                self._x = tempX
                self._y = tempY
            self._listaZdarzen.insert(0,
                str(self) + ' wkracza na pole (' + str(self.getX()) + ',' + str(
                    self.getY()) + ')' + ' wypychajac ' + str(org) + ' za pomoca tarczy Alzura')
        else:
            super(Czlowiek, self)._kolizja(x2, y2)

    def __obsluzTarczeAlzura(self):
        if(self.__tarczaAlzura == 1):
            self.__licznikTarczy += 1
            if self.__licznikTarczy == 5:
                self._listaZdarzen.append('Tarcza Alzura przestaje dzialac')
                self.__tarczaAlzura = 0
                self.__cooldownTarczy = 5
            else:
                self._listaZdarzen.append('Tarcza Alzura aktywna')
        else:
            if self.__cooldownTarczy>0:
                self.__cooldownTarczy -= 1
            if not self.__cooldownTarczy>0:
                self._listaZdarzen.append('Tarcza Alzura gotowa do uzycia')
                pass
