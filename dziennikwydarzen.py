import pygame

class DziennikWydarzen():

    __kolor = (255, 255, 255)

    __scroll = 0

    def __init__(self):
        self.__list = []

    def scroll(self, scrl):
        self.__scroll += scrl

    def dodajWydarzenie(self, str):
        self.__list.append(str)

    def dodajWydarzenieNaPoczatek(self, str):
        self.__list.insert(0, str)

    def wypiszWydarzenia(self, screen, font, upBound, leftBound):
        przesuniecie = 0
        for element in self.__list:
            text = font.render(element, False, self.__kolor)
            screen.blit(text, (leftBound + 10, upBound+przesuniecie + self.__scroll))
            przesuniecie += 20

    def wyczysc(self):
        self.__scroll = 0
        self.__list = []