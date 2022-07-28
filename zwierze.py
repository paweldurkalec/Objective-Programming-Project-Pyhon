from organizm import Organizm
import abc
import random

class Zwierze(Organizm):
    __metaclass__ = abc.ABCMeta

    def __init__(self, minMiedzyRozmnazaniami, kolor, sila, inicjatywa, x, y, mapa):
        super(Zwierze, self).__init__(kolor, sila, inicjatywa, x, y, mapa)
        self.__minMiedzyRozmnazaniami = minMiedzyRozmnazaniami
        self.__odOstatniegoRozmnazania = 0

    def _rysowanie(self):
        self._mapa[self._x][self._y] = self

    def czyTruje(self, org):
        return False

    def czyDajeSile(self, org):
        return False

    def czyOdbilAtak(self, x2, y2):
        return 0

    def czyUcieka(self):
        return False

    def czyZwierze(self):
        return True

    def zwiekszCzasOdOstatniegoRozmnazania(self):
        self.__odOstatniegoRozmnazania += 1

    def szukajMiejscaDoRozrodu(self):
        if self.__odOstatniegoRozmnazania >= self.__minMiedzyRozmnazaniami:
            if super()._czyGdziekolwiekWolne():
                self.__odOstatniegoRozmnazania = 0
                kierunek = random.randint(0, 3)
                newX = self._x
                newY = self._y
                while not super()._czyWolne(kierunek) == 1:
                    kierunek = random.randint(0, 3)
                if kierunek == 0:
                    newY -= 1
                elif kierunek == 1:
                    newX += 1
                elif kierunek == 2:
                    newY += 1
                elif kierunek == 3:
                    newX -= 1
                self._listaZdarzen.append(
                    str(self) + ' rozmnozyly sie na (' + str(self.getX()) + ',' + str(self.getY()) + ')')
                self._rozmnazaj(newX, newY)

    def akcja(self):
        nextX = self._x
        nextY = self._y
        kierunek = random.randint(0, 3)
        if kierunek == 0:
            nextY -= 1
        elif kierunek == 1:
            nextX += 1
        elif kierunek == 2:
            nextY += 1
        elif kierunek == 3:
            nextX -= 1
        rodzajAkcji = self._czyWolne(kierunek)
        if rodzajAkcji == 0:
            self.akcja()
        elif rodzajAkcji == 1:
            self._mapa[self._x][self._y] = 0
            self._x = nextX
            self._y = nextY
            self._wiek += 1
            self.__odOstatniegoRozmnazania += 1
            self._rysowanie()
        elif rodzajAkcji == 2:
            self._kolizja(nextX, nextY)
            self._wiek += 1
            self.__odOstatniegoRozmnazania += 1

    def _rozmnazaj(self, a, b):
        print('nie powinienem tu byc')
        return

    def _zwiekszCzasOdOstRozmn(self):
        self.__odOstatniegoRozmnazania+=1

    def _kolizja(self, x2, y2):
        drugiOrganizm = self._mapa[x2][y2]
        newX = drugiOrganizm.getX()
        newY = drugiOrganizm.getY()
        if type(drugiOrganizm) == type(self):
            if self.__odOstatniegoRozmnazania >= self.__minMiedzyRozmnazaniami:
                self.__odOstatniegoRozmnazania = 0
                drugiOrganizm.szukajMiejscaDoRozrodu()
            return
        if drugiOrganizm.czyOdbilAtak(self._x, self._y) == 1:
            self._listaZdarzen.append(
                str(drugiOrganizm) + ' odbil atak ' + str(self) + ' na (' + str(self.getX()) + ',' + str(
                    self.getY()) + ')')
            return
        elif drugiOrganizm.czyOdbilAtak(self._x, self._y) == 2:
            tempX = self._x
            tempY = self._y
            self._x = x2
            self._y = y2
            if self._czyGdziekolwiekWolne():
                kierunek = random.randint(0, 3)
                nextX = self._x
                nextY = self._y
                while not super()._czyWolne(kierunek) == 1:
                    kierunek = random.randint(0, 3)
                if kierunek == 0:
                    nextY -= 1
                elif kierunek == 1:
                    nextX += 1
                elif kierunek == 2:
                    nextY += 1
                elif kierunek == 3:
                    nextX -= 1
                self._mapa[tempX][tempY] = 0
                self._x = nextX
                self._y = nextY
                self._rysowanie()
            else:
                self._x = tempX
                self._y = tempY
            self._listaZdarzen.append(
                str(drugiOrganizm) + ' wykorzystal tarcze Alzura i odbil atak ' + str(self) + ' na (' + str(
                    self.getX()) + ',' + str(self.getY()) + ')')
            return
        if drugiOrganizm.czyTruje(self):
            self._listaZdarzen.append(
                str(self) + ' zjadl trujace ' + str(drugiOrganizm) + ' na (' + str(self.getX()) + ',' + str(
                    self.getY()) + ')')
            return
        if drugiOrganizm.czyDajeSile(self):
            self._listaZdarzen.append(
                str(self) + ' otrzymal sile, zjadajac ' + str(drugiOrganizm) + ' na (' + str(self.getX()) + ',' + str(
                    self.getY()) + ')')
        if drugiOrganizm.czyUcieka():
            self._mapa[self._x][self._y] = 0
            self._x = newX
            self._y = newY
            self._rysowanie()
            return
        if drugiOrganizm.getSila() <= self.getSila():
            self._mapa[self._x][self._y] = 0
            self._x = newX
            self._y = newY
            self._listaZdarzen.append(
                str(self) + ' pokonal ' + str(drugiOrganizm) + ' na (' + str(self.getX()) + ',' + str(
                    self.getY()) + ')')
            self._rysowanie()
        else:
            self._mapa[self._x][self._y] = 0
            self._listaZdarzen.append(
                str(drugiOrganizm) + ' pokonal ' + str(self) + ' na (' + str(self.getX()) + ',' + str(
                    self.getY()) + ')')
        return