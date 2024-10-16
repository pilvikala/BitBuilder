import pygame

def set_event_handled(event: pygame.event.Event):
  event.dict["handled"] = True
  return event
