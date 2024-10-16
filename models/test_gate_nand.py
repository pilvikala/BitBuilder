from models.gate_nand import GateNAnd

def test_gate_and_function_returns_and():
  gate = GateNAnd()
  assert gate._inputs["A"].value == False
  assert gate._inputs["B"].value == False
  assert gate._outputs["Y"].value == True
  gate.set_input("A", True)
  assert gate._inputs["A"].value == True
  assert gate._inputs["B"].value == False
  assert gate._outputs["Y"].value == True
  gate.set_input("B", True)
  assert gate._inputs["A"].value == True
  assert gate._inputs["B"].value == True
  assert gate._outputs["Y"].value == False
  gate.set_input("A", False)
  assert gate._inputs["A"].value == False
  assert gate._inputs["B"].value == True
  assert gate._outputs["Y"].value == True
  gate.set_input("B", False)
  assert gate._inputs["A"].value == False
  assert gate._inputs["B"].value == False
  assert gate._outputs["Y"].value == True
