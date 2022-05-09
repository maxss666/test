import main_graphics
import Creature_graphics
#зоны

test_l_2 = [[main_graphics.test_class(0, 0, (255, 0, 0)), main_graphics.test_class(0, 1, (0, 255, 0))],
            [main_graphics.test_class(1, 0, (100, 0, 0)), main_graphics.test_class(1, 1, (0, 255, 0))],
            ]

#существа

test_l_creature = [Creature_graphics.Creature(200.0, 11.0, 20, 20, (255, 0, 0), 1),
                   Creature_graphics.Creature(11.0, 200.0, 20, 20, (0, 255, 0), 1),
                   Creature_graphics.Creature(200.0, 200.0, 20, 20, (0, 0, 255), 1),

                  ]


#список новых кординат существ

update_list_of_creature = [[(200.0, 32.0), (32.0, 200.0)],
                            ]

class Start:

    def __init__(self, number_of_columns, number_of_lines, list_of_zone_of_smell, cell_side, LINE_CHIKNESS,
                 list_of_creature, update_list_of_creature):
        """"

        list_of_creature - список из объектов класса Creature


        update_list_of_creature - двумерный список вида [[(200.0, 32.0), (32.0, 200.0), ...],
                                                         [(...), (...), ...],
                                                         ....
                                                         ]
                                    где update_list_of_creature[i][j][0] - 1 первый аргумент функции list_of_creature[j].update()
                                    a update_list_of_creature[i][j][1] - 1 первый аргумент функции list_of_creature[j].update()

        """
        self.number_of_columns = number_of_columns
        self.number_of_lines = number_of_lines
        self.list_of_zone_of_smell = list_of_zone_of_smell
        self.cell_side = cell_side
        self.LINE_CHIKNESS = LINE_CHIKNESS
        self.list_of_creature = list_of_creature
        main_graphics.start_garhics(number_of_columns, number_of_lines, list_of_zone_of_smell, cell_side, LINE_CHIKNESS,
                                    list_of_creature, update_list_of_creature)

start = Start(10, 10, test_l_2, 20, 1, test_l_creature, update_list_of_creature)