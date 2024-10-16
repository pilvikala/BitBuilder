from models.gate_base import GateBase


class GateNot(GateBase):
  def __init__(self):
    super().__init__(["A"], ["Y"])

  def recalculate_output(self):
    self._outputs["Y"].value = not self._inputs["A"].value
