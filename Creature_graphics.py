import pygame


class Creature(pygame.sprite.Sprite):
    """"
    Класс - существо, есть метод update(self, *args) - который принимает две координаты куда ему идти,
    и движется туда (движется по кратчайшему пути  (по прямой))
    """
    def __init__(self, x0, y0, width, length, color, speed = 1):
        pygame.sprite.Sprite.__init__(self)
        sf = pygame.Surface((width, length))
        sf.fill(color)
        self.image = sf
        self.rect = self.image.get_rect(center = (x0, y0))
        self.speed = speed
        self.width = width
        self.length = length

    def update(self, *args) -> None:
        """"
        update(self, *args) - функция, принимающия две координаты и перемещ. объект туда
        :return -> None
        """
        if self.rect.centerx < args[0]:
            if self.rect.centerx < args[0]:
                self.rect.centerx += self.speed
            '''
            if self.rect.centery < args[1]:
                self.rect.centery += self.speed
            '''
        if self.rect.centerx > args[0]:
            if self.rect.centerx > args[0]:
                self.rect.centerx -= self.speed
            '''
            if self.rect.centery > args[1]:
                self.rect.centery -= self.speed
            '''
        if self.rect.centery < args[1]:
            if self.rect.centery < args[1]:
                self.rect.centery += self.speed

        if self.rect.centery > args[1]:
            if self.rect.centery > args[1]:
                self.rect.centery -= self.speed

    def follow_the_route(self, l: list) -> None:
        pass

