from pygame import Surface
from models.gate_type import GateType
from views.gate_view import GateView

class BoardView:
  def __init__(self):
    self.gates_map = {}
    self.gates: list[GateView] = []

  def add_gate(self, id: int, type: GateType, x: int, y: int, z: int):
    view = GateView(id, type, x, y, z)
    self.gates_map[id] = view
    self.gates.append(view)
    return view

  def remove_gate(self, id: int) -> GateView:
    gate = self.gates_map.pop(id)
    self.gates.remove(gate)
    return gate

  def render(self, surface: Surface):
    for gate in self.gates:
      gate.render(surface)
