import pygame

def is_event_handled(event: pygame.event.Event) -> bool:
  return "handled" in event.dict.keys() and event.dict["handled"]
