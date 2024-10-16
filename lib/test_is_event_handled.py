import pygame
from lib.is_event_handled import is_event_handled


def test_returns_false_when_event_handled_flag_is_false():
    event = pygame.event.Event(1)
    event.dict["handled"] = False
    assert is_event_handled(event) is False

def test_returns_true_when_event_is_handled():
    event = pygame.event.Event(1)
    event.dict["handled"] = True
    assert is_event_handled(event) is True

def test_returns_false_when_event_handled_flag_is_not_present():
    event = pygame.event.Event(1)
    assert is_event_handled(event) is False
