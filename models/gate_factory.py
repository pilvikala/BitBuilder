from models.gate_base import GateBase
from models.gate_nand import GateNAnd
from models.gate_type import GateType

class GateFactory:
    @staticmethod
    def create_gate(gate_type: GateType) -> GateBase:
        if gate_type == GateType.NAND:
            return GateNAnd()
        if gate_type == GateType.AND:
            return GateNAnd()
        else:
            raise ValueError(f"Unknown gate type: {gate_type}")
