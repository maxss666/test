import pygame
import numpy as np
from Creature_graphics import Creature
from Map_graphics import Map
from Cell_graphics import Draw_Cell
import bottom_panel_graphics
pygame.init()

i = pygame.display.Info()
width = i.current_w
height = i.current_h


class test_class:
    def __init__(self, x , y, color):
        self.x = x
        self.y = y
        self.color = color

test_l = [(2, 0), (3, 5)]# test list
test_l_2 = [[test_class(0, 0, (255, 0, 0)), test_class(0, 1, (0, 255, 0))],
            [test_class(1, 0, (100, 0, 0)), test_class(1, 1, (0, 255, 0))],
            ]


def start_garhics(number_of_columns, number_of_lines, list_of_zone_of_smell, cell_side, LINE_CHIKNESS, list_of_creature,
                  update_list_of_creature):




    WHITE = (255, 255, 255)
    game = True
    FPS = 60
    screen = pygame.display.set_mode((1050, 600))
    clock = pygame.time.Clock()

    screen.fill((0, 0, 0))

    map = Map(number_of_columns , number_of_lines , cell_side, LINE_CHIKNESS)

    main_map = map.create_map()
    # map.print_info_points()
    screen.blit(main_map, (0, 0))
    map.print_info_points()

    save_list_of_creature = []
    save_list_of_zone_of_smell = []
    paused = False
    while game:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    print("нажата P")
                    paused = not paused
                else:
                    paused = not paused
            '''
            if event.type == pygame.MOUSEMOTION:
                print("Позиция :", event.pos)
            '''
        if paused:
            screen.fill((0, 0, 0))  # заполнение экрана
            bottom_panel = bottom_panel_graphics.BottomPanel(100, 100, (0, 255, 0), (0, 0, 255), screen, 1050, 600)
            main_map = map.create_map()  # заполнение карты
            Draw_Cell(main_map, list_of_zone_of_smell, 20, 20, map.arr)  # трисовка зон

            # отрисовка существ
            for i in list_of_creature:
                rect = i.image.get_rect(center=(i.rect.centerx, i.rect.centery))
                main_map.blit(i.image, rect)

            screen.blit(main_map, (0, 0))  # заполнение экрана
            pygame.display.update()  # flip экрана
            '''
            main_map.fill((0, 0, 0))
            screen.blit(main_map, (0 , 0))
            pygame.display.update()  # flip экрана
            '''
        else:
            screen.fill((0, 0, 0))  # заполнение экрана
            main_map = map.create_map()  # заполнение карты
            Draw_Cell(main_map, list_of_zone_of_smell, 20, 20, map.arr) # трисовка зон

            # отрисовка существ
            for i in list_of_creature:
                rect = i.image.get_rect(center=(i.rect.centerx, i.rect.centery))
                main_map.blit(i.image, rect)

            screen.blit(main_map, (0, 0))  # заполнение экрана
            pygame.display.update()  # flip экрана

            ''''
            обновление кординат
            '''
            for i in range(0,len(update_list_of_creature)):
                for j in range(0 , len(update_list_of_creature[i])):
                    list_of_creature[j].update(update_list_of_creature[i][j][0], update_list_of_creature[i][j][1])

            #list_of_creature[0].update(200.0, 32.0)



        #creature1.update_top(390.0, 349.0)  # изменение координат


#start_garhics(2, 2, test_l_2, 20)

