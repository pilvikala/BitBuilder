import pygame
from lib.is_event_handled import is_event_handled
from models.board import Board
from models.gate_factory import GateFactory
from models.gate_type import GateType
from views.board_view import BoardView
from views.gate_view import GateView
from views.sprite_with_events import SpriteEvents, SpriteWithEvents

class BoardController:
  def __init__(self, board: Board, board_view: BoardView):
    self.model = board
    self.view = board_view
    self.sprite_group = pygame.sprite.Group()

  def add_gate(self, gate_type:GateType, x: int, y: int, z: int):
    gate = GateFactory.create_gate(gate_type)
    self.model.add_gate(gate)
    gate_view = self.view.add_gate(gate.id, gate_type, x,y,z)
    gate_view.notifier.subscribe(SpriteEvents.MOUSE_UP, self.on_gate_mouse_up)
    self.sprite_group.add(gate_view)
    print(f"added gate {gate_type} to {x}/{y}")

  def on_gate_mouse_up(self, source: GateView, event: pygame.event.Event):
    print(f"Gate {source.id} clicked: {event}")

  def remove_gate(self, gate_id: int):
    self.model.remove_gate(gate_id)
    sprite = self.view.remove_gate(gate_id)
    self.sprite_group.remove(sprite)
    sprite.notifier.remove_all_subscribers()

  def on_event(self, event: pygame.event.Event):
    self.sprite_group.update([event])
    if is_event_handled(event):
      return
    if event.type == pygame.MOUSEBUTTONUP:
      if event.button == 1:
          self.add_gate(GateType.AND, event.pos[0], event.pos[1], 0)
    else:
      print(f"Unhandled Event: {event}")
