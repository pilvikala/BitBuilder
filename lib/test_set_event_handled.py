from lib.is_event_handled import is_event_handled
from lib.set_event_handled import set_event_handled
import pygame

def test_sets_handled_flag_to_true():
    event = pygame.event.Event(1)
    set_event_handled(event)
    assert is_event_handled(event) is True
