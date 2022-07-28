import pygame

class Przycisk:

    def __init__(self, screen, text, pos, tlo, org="None"):
        self.__org = org
        self.__screen = screen
        self.__x, self.__y = pos
        self.__font = pygame.font.SysFont("Comic Sans MS", 20)
        self.__text = self.__font.render(text, True, pygame.Color("Black"))
        self.__size = self.__text.get_size()
        self.__szer = self.__size[0]
        self.__wys = self.__size[1]
        self.__surface = pygame.Surface(self.__size)
        self.__surface.fill(tlo)
        self.__surface.blit(self.__text, (0, 0))
        self.__rect = pygame.Rect(self.__x, self.__y, self.__size[0], self.__size[1])

    def getSzer(self):
        return self.__szer

    def getOrg(self):
        return self.__org

    def getWys(self):
        return self.__wys

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def czyNacisniety(self):
        x, y = pygame.mouse.get_pos()
        if self.__rect.collidepoint(x, y):
            return 1
        return 0

    def rysuj(self):
        self.__screen.blit(self.__surface, (self.__x, self.__y))