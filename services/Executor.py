import utils.Constants as const
from services.Decoder import Decoder
from services.executors.ITypeStrategy import ITypeStrategy
from services.executors.RTypeStrategy import RTypeStrategy

class Executor:
    def __init__(self, regs) -> None:
        self.I_type = ITypeStrategy(regs)
        self.R_type = RTypeStrategy(regs)

    def execute(self, instr, log_info) -> int:
        opcode = Decoder.opcode(instr)

        if opcode == const.LUI:
            self.execute_LUI(instr, log_info)
        elif opcode == const.AUIPC:
            self.execute_AUIPC(instr, log_info)
        elif opcode == const.JAL:
            self.execute_JAL(instr, log_info)
        elif opcode == const.JALR:
            self.execute_JALR(instr, log_info)
        elif opcode == const.LOAD:
            self.execute_LOAD(instr, log_info)
        elif opcode == const.FENCE:
            self.execute_FENCE(instr, log_info)
        elif opcode == const.B_TYPE:
            self.execute_B_TYPE(instr, log_info)
        elif opcode == const.R_TYPE:
            self.R_type.execute(instr, log_info)
        elif opcode == const.I_TYPE:
            self.I_type.execute(instr, log_info)
        elif opcode == const.C_TYPE:
            self.execute_C_TYPE(instr, log_info)
        elif opcode == const.S_TYPE:
            self.execute_S_TYPE(instr, log_info)
        else:
            raise Exception('Cannot decode instruction type')
        
        return 1