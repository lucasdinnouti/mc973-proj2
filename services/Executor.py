import utils.Constants as const
from services.Decoder import Decoder
from services.executors.ITypeStrategy import ITypeStrategy

class Executor:
    def __init__(self, regs) -> None:
        self.I_type = ITypeStrategy(regs)

    def execute(self, instr, log_info) -> int:
        opcode = Decoder.opcode(instr)
        funct3 = Decoder.funct3(instr)
        funct7 = Decoder.funct7(instr)

        if opcode == const.LUI:
            self.execute_LUI(instr, funct3, funct7, log_info)
        elif opcode == const.AUIPC:
            self.execute_AUIPC(instr, funct3, funct7, log_info)
        elif opcode == const.JAL:
            self.execute_JAL(instr, funct3, funct7, log_info)
        elif opcode == const.JALR:
            self.execute_JALR(instr, funct3, funct7, log_info)
        elif opcode == const.LOAD:
            self.execute_LOAD(instr, funct3, funct7, log_info)
        elif opcode == const.FENCE:
            self.execute_FENCE(instr, funct3, funct7, log_info)
        elif opcode == const.B_TYPE:
            self.execute_B_TYPE(instr, funct3, funct7, log_info)
        elif opcode == const.R_TYPE:
            self.execute_R_TYPE(instr, funct3, funct7, log_info)
        elif opcode == const.I_TYPE:
            self.I_type.execute(instr, funct3, funct7, log_info)
        elif opcode == const.C_TYPE:
            self.execute_C_TYPE(instr, funct3, funct7, log_info)
        elif opcode == const.S_TYPE:
            self.execute_S_TYPE(instr, funct3, funct7, log_info)
        else:
            raise Exception('Cannot decode instruction type')
        
        return 1