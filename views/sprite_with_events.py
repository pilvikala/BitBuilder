import pygame
from enum import Enum
from EventNotifier import Notifier
from lib.is_event_handled import is_event_handled
from lib.set_event_handled import set_event_handled

class SpriteEvents(Enum):
  MOUSE_UP = "on_mouse_up"

class SpriteWithEvents(pygame.sprite.Sprite):

  def __init__(self, image: pygame.surface.Surface, x, y):
    super().__init__()
    self.image = image
    self.rect = self.image.get_rect()
    self.rect.center = (x, y)
    self.notifier = Notifier([SpriteEvents.MOUSE_UP])

  def raise_on_mouse_up(self, event: pygame.event.Event):
    print(SpriteEvents.MOUSE_UP, event)
    self.notifier.raise_event(SpriteEvents.MOUSE_UP, self, event)

  def update(self, events: list[pygame.event.Event]):
    for event in events:
      if is_event_handled(event):
        continue
      if event.type == pygame.MOUSEBUTTONUP:
        if self.rect.collidepoint(event.pos):
          set_event_handled(event)
          self.raise_on_mouse_up(event)
