from services.executors.ExecutionStrategy import ExecutionStrategy
from utils.Logger import LogInfo
from services.Decoder import Decoder
import utils.Constants as const

class ITypeStrategy(ExecutionStrategy):
    def execute(self, instr, funct3, funct7, log_info: LogInfo) -> int:
        if funct3 == const.ADDI:
            self.exec_ADDI(instr, log_info)
        elif funct3 == const.SLLI:
            self.exec_SLLI(instr, log_info)
        elif funct3 == const.SLTI:
            self.exec_SLTI(instr, log_info)
        elif funct3 == const.SLTIU:
            self.exec_SLTIU(instr, log_info)
        elif funct3 == const.XORI:
            self.exec_XORI(instr, log_info)
        elif funct3 == const.SRI:
            if funct7 == const.SRLI:
                self.exec_SRLI(instr, log_info)
            elif funct7 == const.SRAI:
                self.exec_SRAI(instr, log_info)
        elif funct3 == const.ORI:
            self.exec_ORI(instr, log_info)
        elif funct3 == const.ANDI:
            self.exec_ANDI(instr, log_info)
        else:
            raise Exception('Cannot decode I_TYPE instruction')

    def exec_ADDI(self, instr, log_info: LogInfo):
        imm = Decoder.imm_I(instr)
        rd = Decoder.rd(instr)
        rs1 = Decoder.rs1(instr)
        self.regs[rd] = self.regs[rs1] + imm

        log_info.set_rd(rd, self.regs[rd])
        log_info.set_rs1(rs1, self.regs[rs1])
        log_info.set_disassembly(f'addi	x{rd}, x{rs1}, {imm}')

    def exec_SLLI(self, instr, log_info: LogInfo):
        pass

    def exec_SLTI(self, instr, log_info: LogInfo):
        pass

    def exec_SLTIU(self, instr, log_info: LogInfo):
        pass

    def exec_XORI(self, instr, log_info: LogInfo):
        pass

    def exec_SRLI(self, instr, log_info: LogInfo):
        pass

    def exec_SRAI(self, instr, log_info: LogInfo):
        pass

    def exec_ORI(self, instr, log_info: LogInfo):
        pass

    def exec_ANDI(self, instr, log_info: LogInfo):
        pass
