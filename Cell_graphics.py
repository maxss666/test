import pygame


def Draw_Cell(main_sf: pygame.Surface, list_of_zone_of_smell, width, length, map):
    """
    Отрисовка всех зон запахов
    :param main_sf: тот surface на котором надо нарисовать клетку
    :param list_of_zone_of_smell: двойной список(таокого-же размера как и map), содержащий клетки
    :param width: ширина клетки
    :param length: длина клеткиdwdwdsdsdffndnckdcndnc
    :param map: двойной список элемент каждого - кортеж координат клетки на полке
    :return: None
    ""svvdvd"
    for i in list_of_zone_of_smell:
        for j in i:
            sf_сell = pygame.Surface((width, length))
            sf_сell.fill(j.color)
            rect = sf_сell.get_rect(center=(map[j.y][j.y].x, map[j.x][j.y].y))
            main_sf.blit(sf_сell, rect)



