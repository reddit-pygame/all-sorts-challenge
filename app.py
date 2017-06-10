import sys

import pygame as pg


class App(object):
    def __init__(self, screen_size):
        self.done = False
        self.screen = pg.display.set_mode(screen_size)
        self.clock = pg.time.Clock()
        self.fps = 60
        self.bg_color = pg.Color("gray5")
        
    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
                
    def update(self, dt):
        pass
        
    def draw(self):
        self.screen.fill(self.bg_color)
        
    def run(self):
        while not self.done:
            dt = self.clock.tick(self.fps)
            self.event_loop()
            self.update(dt)
            self.draw()
            pg.display.update()
            
       
if __name__ == "__main__":
    game = App((1280, 720))
    game.run()
    pg.quit()
    sys.exit()