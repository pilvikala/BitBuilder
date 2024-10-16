from models.board import Board
import unittest
from models.gate_and import GateAnd

class TestBoard(unittest.TestCase):
  def setUp(self):
    self.board = Board()
    self.gate_and = GateAnd()

  def tearDown(self):
    del self.board
    del self.gate_and

  def test_add_gate(self):
    gate_id = self.board.add_gate(self.gate_and)
    self.assertEqual(gate_id, self.gate_and.id)

  def test_remove_gate(self):
    gate_id = self.board.add_gate(self.gate_and)
    self.board.remove_gate(gate_id)
    self.assertNotIn(gate_id, self.board._gates_map)

  def test_set_gate_input(self):
    gate_id = self.board.add_gate(self.gate_and)
    self.board.set_gate_input(gate_id, 'A', True)
    self.assertTrue(self.gate_and._inputs['A'].value)
