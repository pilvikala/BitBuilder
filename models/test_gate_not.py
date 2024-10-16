from models.gate_not import GateNot

def test_gate_not_function_returns_not():
  gate = GateNot()
  assert gate._inputs["A"].value == False
  assert gate._outputs["Y"].value == True
  gate.set_input("A", True)
  assert gate._inputs["A"].value == True
  assert gate._outputs["Y"].value == False
