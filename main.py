import pygame
from pygame.locals import *

from controllers.board_controller import BoardController
from models.board import Board
from views.board_view import BoardView

class App:
    def __init__(self):
      self._running = True
      self._surface = None
      pygame.display.set_mode((0,0), pygame.FULLSCREEN)
      display_info = pygame.display.Info()
      self.size = self.weight, self.height = display_info.current_w, display_info.current_h

    def on_init(self):
      pygame.init()
      self._surface = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
      FPS = pygame.time.Clock()
      FPS.tick(60)

      self.board = Board()
      self.board_view = BoardView()
      self.board_controller = BoardController(self.board, self.board_view)
      self._running = True

    def on_event(self, event):
      if event.type == pygame.QUIT:
        self._running = False
      else:
        self.board_controller.on_event(event)

    def on_loop(self):
      pass

    def on_render(self):
      self.board_view.render(self._surface)
      pygame.display.update()
      pass

    def on_cleanup(self):
      self.board_view = None
      self.board = None
      pygame.quit()

    def on_execute(self):
      if self.on_init() == False:
        self._running = False

      while( self._running ):
        for event in pygame.event.get():
          self.on_event(event)
        self.on_loop()
        self.on_render()
      self.on_cleanup()

if __name__ == "__main__" :
  theApp = App()
  theApp.on_execute()
