import pygame

class BottomPanel:
    def __init__(self, width, length, color_panel, color_text_pause, main_sf, width_main_sf, lenght_main_sf):
        self.sf = pygame.Surface((width, length))
        # self.sf.fill(color_panel)
        self.width = width
        self.length = length
        self.color_panel = color_panel
        self.color_text_pause = color_text_pause
        self.main_sf = main_sf
        self.lenght_main_sf = lenght_main_sf
        a = self.create_text_pause()
        main_sf.blit(a[0], a[1])

    def create_text_pause(self):
        f = pygame.font.SysFont('arial', 20)
        sc_text = f.render('pause', 1, self.color_text_pause, self.color_panel)
        pos = sc_text.get_rect(bottomleft= (0, self.lenght_main_sf))
        #self.sf.blit(sc_text, pos)
        return sc_text, pos

