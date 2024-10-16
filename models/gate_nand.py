from models.gate_base import GateBase

class GateNAnd(GateBase):

  def __init__(self):
    super().__init__(["A", "B"], ["Y"])

  def recalculate_output(self):
    self._outputs["Y"].value = not (self._inputs["A"].value and self._inputs["B"].value)
