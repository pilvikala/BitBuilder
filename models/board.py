from models.gate_base import GateBase

class Board:
  _gates: list[GateBase]
  _gates_map: dict[int, GateBase]

  def __init__(self):
    self._gates = []
    self._gates_map = {}

  def add_gate(self, gate: GateBase) -> int:
    self._gates.append(gate)
    self._gates_map[gate.id] = gate
    return gate.id

  def remove_gate(self, gate_id: int):
    self._gates.remove(self._gates_map[gate_id])
    self._gates_map.pop(gate_id)

  def set_gate_input(self, gate_id: int, input_name: str, value: bool):
    self._gates_map[gate_id].set_input(input_name, value)

  def get_gate_output(self, gate_id: int, output_name: str) -> bool:
    return self._gates_map[gate_id]._outputs[output_name].value
