import pygame
import os
import time
import random
from czlowiek import Czlowiek
from owca import Owca
from wilk import Wilk
from trawa import Trawa
from mlecz import Mlecz
from wilczejagody import WilczeJagody
from guarana import Guarana
from barszczsosnowskiego import BarszczSosnowskiego
from lis import Lis
from zolw import Zolw
from antylopa import Antylopa
from cyberowca import CyberOwca
from dziennikwydarzen import DziennikWydarzen
from przycisk import Przycisk

class Swiat():

    __recSize = 20
    __rectangle = pygame.Rect(10, 10, __recSize, __recSize)
    __upperBound = 70
    __leftBound = 50
    __frameThick = 5
    __frameColour = (255, 255, 255)
    __exit = False
    __wybranyOrganizm = 0

    def __init__(self):
        if not os.path.exists('config.txt'):
            print("Brak pliku config.txt!")
            self.__exit = 1
        else:
            configFile = open("config.txt", "r")
            config = configFile.read().split()
            iloscZwierzat=0
            for i in range(9, 29, 2):
                iloscZwierzat += int(config[i])
            self.__resX = int(config[1])
            self.__resY = int(config[3])
            self.__x = int(config[5])
            self.__y = int(config[7])
            if iloscZwierzat + 1 > self.__x*self.__y:
                print("Suma zwierzat przekracza sume wolnych pol")
                self.__exit = 1
            else:
                configFile.close()
                self.__res = (self.__resX, self.__resY)
                self.__frame = (self.__leftBound, self.__upperBound, self.__x*self.__recSize+2*self.__frameThick, self.__y*self.__recSize+2*self.__frameThick)
                self.__resetujMape()
                self.__inicjujZycie()
                pygame.init()
                pygame.font.init()
                self.__font = pygame.font.SysFont('Comic Sans MS', 20)
                self.__screen = pygame.display.set_mode(self.__res)
                self.__turaPrzycisk = Przycisk(self.__screen, "Nastepna tura", (self.__leftBound,
                    self.__y*self.__recSize+2*self.__frameThick + self.__upperBound + self.__frameThick), "Grey")
                self.__inicjujLegende()
                pygame.display.set_caption('Symulacja Pawel Durkalec 184773')
                self.rysujSwiat()

    def wykonajTure(self):
        #self.__obsluzKlawiature()
        time.sleep(0.1)
        if not self.__exit:
            self.__dziennik.wyczysc()
            self.__obsluzAkcje()
            self.rysujSwiat()

    def rysujSwiat(self):
        if not self.__exit:
            self.__screen.fill((0,0,0))
            pygame.draw.rect(self.__screen, self.__frameColour, self.__frame, self.__frameThick)
            for i in range(0, self.__x):
                for j in range(0, self.__y):
                    if self.__mapa[i][j] != 0:
                        pygame.draw.rect(self.__screen, self.__mapa[i][j].getColour(), (self.__leftBound + self.__recSize * self.__mapa[i][j].getX() + self.__frameThick, self.__upperBound + self.__recSize * self.__mapa[i][j].getY() + self.__frameThick, self.__recSize, self.__recSize))
            self.__dziennik.wypiszWydarzenia(self.__screen, self.__font, self.__upperBound,
                                             self.__x * self.__recSize + 2 * self.__frameThick + self.__leftBound)
            self.__turaPrzycisk.rysuj()
            self.__rysujLegende()
            pygame.display.flip()

    def getExit(self):
        return self.__exit

    def __rysujLegende(self):
        for i in range(12):
            self.__legenda[i].rysuj()
            if self.__legenda[i].getOrg() == self.__wybranyOrganizm:
                rect = (self.__legenda[i].getX(), self.__legenda[i].getY(), self.__legenda[i].getSzer(), self.__legenda[i].getWys())
                pygame.draw.rect(self.__screen, self.__frameColour, rect, 2)

    def __inicjujLegende(self):
        orgs = [
            ['Guarana', (127, 0, 255)],
            ['Antylopa', (139, 69, 19)],
            ['WilczeJagody', (255, 40, 0)],
            ['CyberOwca', (0, 0, 255)],
            ['Czlowiek', (0, 255, 255)],
            ['Owca', (255, 250, 250)],
            ['Lis', (255, 131, 0)],
            ['Mlecz', (249, 215, 28)],
            ['Trawa', (0, 154, 23)],
            ['BarszczSosnowskiego', (153, 51, 102)],
            ['Wilk', (105, 105, 105)],
            ['Zolw', (215, 252, 0)]
        ]
        self.__legenda = []
        wys = 5
        szer = self.__leftBound
        for i in range(12):
            p = Przycisk(self.__screen, orgs[i][0], (szer, wys), orgs[i][1], orgs[i][0])
            szer += p.getSzer() + 5
            self.__legenda.append(p)
            if i == 4:
                szer = self.__leftBound
                wys += self.__legenda[0].getWys() + 2


    def __znajdzPustePole(self, pustePole):
        pustePole[0] = random.randint(0, self.__x - 1)
        pustePole[1] = random.randint(0, self.__y - 1)
        while self.__mapa[pustePole[0]][pustePole[1]] != 0:
            pustePole[0] = random.randint(0, self.__x - 1)
            pustePole[1] = random.randint(0, self.__y - 1)

    def __inicjujZycie(self):
        configFile = open("config.txt", "r")
        config = configFile.read().split()
        pustePole = [0, 0]
        self.__czlowiek = Czlowiek(self.__mapa)
        self.__dziennik = DziennikWydarzen()
        for i in range(int(config[9])):
            self.__znajdzPustePole(pustePole)
            Owca(self.__mapa, pustePole[0], pustePole[1])
        for i in range(int(config[11])):
            self.__znajdzPustePole(pustePole)
            Wilk(self.__mapa, pustePole[0], pustePole[1])
        for i in range(int(config[13])):
            self.__znajdzPustePole(pustePole)
            Trawa(self.__mapa, pustePole[0], pustePole[1])
        for i in range(int(config[15])):
            self.__znajdzPustePole(pustePole)
            Mlecz(self.__mapa, pustePole[0], pustePole[1])
        for i in range(int(config[17])):
            self.__znajdzPustePole(pustePole)
            WilczeJagody(self.__mapa, pustePole[0], pustePole[1])
        for i in range(int(config[19])):
            self.__znajdzPustePole(pustePole)
            Guarana(self.__mapa, pustePole[0], pustePole[1])
        for i in range(int(config[21])):
            self.__znajdzPustePole(pustePole)
            BarszczSosnowskiego(self.__mapa, pustePole[0], pustePole[1])
        for i in range(int(config[23])):
            self.__znajdzPustePole(pustePole)
            Zolw(self.__mapa, pustePole[0], pustePole[1])
        for i in range(int(config[25])):
            self.__znajdzPustePole(pustePole)
            Lis(self.__mapa, pustePole[0], pustePole[1])
        for i in range(int(config[27])):
            self.__znajdzPustePole(pustePole)
            Antylopa(self.__mapa, pustePole[0], pustePole[1])
        for i in range(int(config[29])):
            self.__znajdzPustePole(pustePole)
            CyberOwca(self.__mapa, pustePole[0], pustePole[1])
        configFile.close()

    def __obsluzAkcje(self):
        tempList = []
        for i in range(0, self.__x):
            for j in range(0, self.__y):
                if self.__mapa[i][j] != 0:
                    tempList.append(self.__mapa[i][j])

        tempList.sort(key=lambda x: (x.getInit(), x.getWiek()), reverse=True)

        for element in tempList:
            if element == self.__mapa[element.getX()][element.getY()]:
                element.akcja()
            element.umiescZdarzeniaWDzienniku(self.__dziennik)

    def __resetujMape(self):
        self.__mapa = []
        for i in range(0, self.__x):
            z = []
            for j in range(0, self.__y):
                z.append(0)
            self.__mapa.append(z)

    def __zapisz(self):
        file = open("zapis.txt", "w")
        file.write(str(self.__x) + ' ' + str(self.__y) + '\n')
        for i in range(0, self.__x):
            for j in range(0, self.__y):
                if self.__mapa[i][j] != 0:
                    self.__mapa[i][j].zapisz(file)

        self.__dziennik.wyczysc()
        self.__dziennik.dodajWydarzenieNaPoczatek('Zapisano stan rozgrywki')
        self.rysujSwiat()
        file.close()

    def __wczytaj(self):
        classDict = {
            'owca': 'Owca',
            'antylopa': 'Antylopa',
            'barszcz_sosnowskiego': 'BarszczSosnowskiego',
            'cyber-owca': 'CyberOwca',
            'czlowiek': 'Czlowiek',
            'guarana': 'Guarana',
            'lis': 'Lis',
            'mlecz': 'Mlecz',
            'trawa': 'Trawa',
            'wilcze_jagody': 'WilczeJagody',
            'wilk': 'Wilk',
            'zolw': 'Zolw'
        }
        if not os.path.exists('zapis.txt'):
            return

        i = 0
        with open("zapis.txt", "r") as f:
            for line in f:
                items = line.split()
                if i == 0:
                    self.__x = int(items[0])
                    self.__y = int(items[1])
                    self.__frame = (self.__leftBound, self.__upperBound, self.__x * self.__recSize + 2 * self.__frameThick,
                                    self.__y * self.__recSize + 2 * self.__frameThick)
                    self.__turaPrzycisk = Przycisk(self.__screen, "Nastepna tura", (self.__leftBound,
                        self.__y * self.__recSize + 2 * self.__frameThick + self.__upperBound + self.__frameThick), "Grey")
                    self.__resetujMape()
                    self.__inicjujLegende()
                    i = 1
                else:
                    klass = globals()[classDict[items[0]]]
                    if items[0] == 'czlowiek':
                        org = klass(self.__mapa, int(items[1]), int(items[2]), int(items[5]), int(items[6]),
                                    int(items[7]), int(items[8]))
                        self.__czlowiek = org
                    else:
                        org = klass(self.__mapa, int(items[1]), int(items[2]))
                    org.setSila(int(items[3]))
                    org.setWiek(int(items[4]))

        self.__dziennik.wyczysc()
        self.__dziennik.dodajWydarzenieNaPoczatek('Wczytano stan rozgrywki')
        self.rysujSwiat()
        f.close()

    def __nacisnietePole(self):
        x, y = pygame.mouse.get_pos()
        szer = self.__leftBound + self.__frameThick
        for i in range(0, self.__x):
            wys = self.__upperBound + self.__frameThick
            for j in range(0, self.__y):
                if x >= szer and x <= szer + self.__recSize and y >= wys and y <= wys + self.__recSize:
                    return(i, j)
                wys += self.__recSize
            szer += self.__recSize
        return (-1, -1)

    def __obsluzDodawanieOrganizmow(self, a, b):
        if a != -1 and self.__wybranyOrganizm != 0 and self.__wybranyOrganizm != "Czlowiek":
            klass = globals()[self.__wybranyOrganizm]
            if self.__mapa[a][b] == 0:
                klass(self.__mapa, a, b)
                self.__dziennik.dodajWydarzenie(
                    'Dodano ' + self.__wybranyOrganizm + ' na (' + str(a) + ',' + str(b) + ')')
        elif a != -1 and self.__wybranyOrganizm != 0 and self.__wybranyOrganizm == "Czlowiek":
            if self.__mapa[a][b] == 0:
                if self.__mapa[self.__czlowiek.getX()][self.__czlowiek.getY()] != self.__czlowiek:
                    self.__czlowiek = Czlowiek(self.__mapa, a, b)
                    self.__dziennik.dodajWydarzenie(
                        'Dodano ' + self.__wybranyOrganizm + ' na (' + str(a) + ',' + str(b) + ')')
        self.rysujSwiat()


    def __obsluzKlawiature(self):
        q = 0
        while not q:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__exit = True
                    q = 1
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.__exit = True
                        q = 1

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.__turaPrzycisk.czyNacisniety():
                            q = 1
                        else:
                            for przycisk in self.__legenda:
                                if przycisk.czyNacisniety():
                                    self.__wybranyOrganizm = przycisk.getOrg()
                                    break
                            a, b = self.__nacisnietePole()
                            self.__obsluzDodawanieOrganizmow(a, b)
                    elif event.button == 4:
                        self.__dziennik.scroll(20)
                    elif event.button == 5:
                        self.__dziennik.scroll(-20)
                    self.rysujSwiat()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.__czlowiek.setKierunek(0)
                    elif event.key == pygame.K_RIGHT:
                        self.__czlowiek.setKierunek(1)
                    elif event.key == pygame.K_DOWN:
                        self.__czlowiek.setKierunek(2)
                    elif event.key == pygame.K_LEFT:
                        self.__czlowiek.setKierunek(3)
                    elif event.key == pygame.K_q:
                        q = 1
                    elif event.key == pygame.K_w:
                        if self.__czlowiek.getTarcza() == 0 and self.__czlowiek.getCooldownTarczy() == 0:
                            self.__czlowiek.setTarcza(1)
                            self.__czlowiek.resetLicznikTarczy()
                    elif event.key == pygame.K_s:
                        self.__zapisz()
                    elif event.key == pygame.K_r:
                        self.__wczytaj()


            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_q]:
                time.sleep(0.1)
                q = 1

