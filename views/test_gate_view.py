from gate_view import GateView
from models.gate_type import GateType
import pytest

def test_returns_asset_file_name():
    assert GateView.get_asset_name(GateType.AND) == "assets/gate_and.png"
    assert GateView.get_asset_name(GateType.NOT) == "assets/gate_not.png"
    assert GateView.get_asset_name(GateType.NAND) == "assets/gate_nand.png"

def test_throws_error_when_asset_file_doesnt_exist():
    with pytest.raises(Exception) as e_info:
      GateView(1, GateType.Unknown, 1, 1, 1)
    assert e_info.match("Asset does not exist: 'assets/gate_unknown.png'")

def test_creates_gate_view():
    gate = GateView(1, GateType.AND, 1, 1, 1)
    assert gate.id == 1
    assert gate.rect.centerx == 1
    assert gate.rect.centery == 1
    assert gate.z == 1
    assert gate.type == GateType.AND
    assert gate.image is not None
    assert gate.rect is not None
