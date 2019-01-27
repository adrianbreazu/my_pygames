import pygame
import random

MOVE_STEP = 10

class App:
    def __init__(self, width, height):
        self._running = True
        self._width = width
        self._height = height
        self._display_surf = None
        self.size = self.width, self.height = width, height       
        self._background = None 
        self._self_img = pygame.image.load("img/babytux.png")
        self._monster = pygame.image.load("img/xmonster.png")
        self._xpos = 50
        self._ypos = 50
    
    def on_init(self):
        pygame.init()
        pygame.display.set_caption("My first game")
        self._display_surf = pygame.display.set_mode(self.size, pygame.DOUBLEBUF)
        self._running = True
        self.draw()

    def draw(self):
        self._background = pygame.Surface(self._display_surf.get_size())
        self._background.fill((255,255,255))
        self._background = self._background.convert()
        #self._display_surf.blit(self._monster, (random.randint(1, self._width), random.randint(1, self._height)))        

    def on_event(self, event):
        pressedkeys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            self._running = False

        if pressedkeys[pygame.K_LEFT]:
            self._xpos -= MOVE_STEP
            if self._xpos < 0:
                self._xpos = self._width
        elif pressedkeys[pygame.K_RIGHT]:
            self._xpos += MOVE_STEP
            if self._xpos > self._width:
                self._xpos = 0
        elif pressedkeys[pygame.K_UP]:
            self._ypos -= MOVE_STEP
            if self._ypos < 0:
                self._ypos = self.height
        elif pressedkeys[pygame.K_DOWN]:
            self._ypos += MOVE_STEP
            if self._ypos > self.height:
                self._ypos = 0
    
    def on_loop(self):
        pass

    def on_render(self):
        pass

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False
        
        while(self._running):
            for event in pygame.event.get():
                self.on_event(event)
            
            self._display_surf.blit(self._background, (0, 0))
            self._display_surf.blit(self._self_img, (self._xpos,self._ypos))
            pygame.display.flip()
            self.on_loop()
            self.on_render()
        self.on_cleanup()

if __name__ == "__main__":
    app = App(640,400);
    app.on_execute()
