from models.named_io import NamedIO


class GateBase:
  global_id = 0

  id: str
  _inputs: dict[str, NamedIO]
  _outputs: dict[str, NamedIO]

  @staticmethod
  def get_id():
    GateBase.global_id += 1
    return GateBase.global_id

  def init_io(self, io: list[str]):
    return {name: NamedIO(name, False) for name in io}

  def __init__(self, inputs: list[str], outputs: list[str]):
    self.id = GateBase.get_id()
    self._inputs = self.init_io(inputs)
    self._outputs = self.init_io(outputs)
    self.recalculate_output()

  def set_input(self, name: str, value: bool):
    self._inputs[name].value = value
    self.recalculate_output()

  def recalculate_output(self):
    pass
