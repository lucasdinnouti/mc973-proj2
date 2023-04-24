from services.executors.ExecutionStrategy import ExecutionStrategy
from utils.Logger import LogInfo
from services.Decoder import Decoder
import utils.Constants as const

class BTypeStrategy(ExecutionStrategy):
    def execute(self, instr, log_info: LogInfo) -> int:
        funct3 = Decoder.funct3(instr)

        if funct3 == const.BEQ:
            self.exec_BEQ(instr, log_info)
        elif funct3 == const.BNE:
            self.exec_BNE(instr, log_info)
        elif funct3 == const.BLT:
            self.exec_BLT(instr, log_info)
        elif funct3 == const.BGE:
            self.exec_BGE(instr, log_info)
        elif funct3 == const.BLTU:
            self.exec_BLTU(instr, log_info)
        elif funct3 == const.BGEU:
            self.exec_BGEU(instr, log_info)
        else:
            raise Exception('Cannot decode B_TYPE instruction')
    
    def exec_BEQ(self, instr, log_info: LogInfo):

        imm = Decoder.imm_B(instr)
        rs1 = Decoder.rs1(instr)
        rs2 = Decoder.rs2(instr)

        rs1_value = self.get(rs1)
        rs2_value = self.get(rs2) 

        if rs1_value == rs2_value:
            self.cpu.pc = imm

        log_info.set_pc(imm)
        log_info.set_rs1(rs1, rs1_value)
        log_info.set_rs2(rs2, rs2_value)
        log_info.set_disassembly(f'beq x{rs1}, x{rs2}, {imm}')

    def exec_BNE(self, instr, log_info: LogInfo):

        imm = Decoder.imm_B(instr)
        rs1 = Decoder.rs1(instr)
        rs2 = Decoder.rs2(instr)

        rs1_value = self.get(rs1)
        rs2_value = self.get(rs2) 

        if rs1_value != rs2_value:
            self.cpu.pc = imm

        log_info.set_pc(imm)
        log_info.set_rs1(rs1, rs1_value)
        log_info.set_rs2(rs2, rs2_value)
        log_info.set_disassembly(f'beq x{rs1}, x{rs2}, {imm}')

    def exec_BLT(self, instr, log_info: LogInfo):
        imm = Decoder.imm_B(instr)
        rs1 = Decoder.rs1(instr)
        rs2 = Decoder.rs2(instr)

        rs1_value = self.get(rs1)
        rs2_value = self.get(rs2) 

        if rs1_value < rs2_value:
            self.cpu.pc = imm

        log_info.set_pc(imm)
        log_info.set_rs1(rs1, rs1_value)
        log_info.set_rs2(rs2, rs2_value)
        log_info.set_disassembly(f'blt x{rs1}, x{rs2}, {imm}')

    def exec_BGE(self, instr, log_info: LogInfo):
        imm = Decoder.imm_B(instr)
        rs1 = Decoder.rs1(instr)
        rs2 = Decoder.rs2(instr)

        rs1_value = self.get(rs1)
        rs2_value = self.get(rs2) 

        if rs1_value >= rs2_value:
            self.cpu.pc = imm

        log_info.set_pc(imm)
        log_info.set_rs1(rs1, rs1_value)
        log_info.set_rs2(rs2, rs2_value)
        log_info.set_disassembly(f'bge x{rs1}, x{rs2}, {imm}')

    def exec_BLTU(self, instr, log_info: LogInfo):
        imm = Decoder.imm_B(instr)
        rs1 = Decoder.rs1(instr)
        rs2 = Decoder.rs2(instr)

        rs1_value = self.get(rs1, unsigned=True)
        rs2_value = self.get(rs2, unsigned=True) 

        if rs1_value < rs2_value:
            self.cpu.pc = imm

        log_info.set_pc(imm)
        log_info.set_rs1(rs1, self.get(rs1))
        log_info.set_rs2(rs2, self.get(rs2))
        log_info.set_disassembly(f'bltu x{rs1}, x{rs2}, {imm}')

    def exec_BGEU(self, instr, log_info: LogInfo):
        imm = Decoder.imm_B(instr)
        rs1 = Decoder.rs1(instr)
        rs2 = Decoder.rs2(instr)

        rs1_value = self.get(rs1, unsigned=True)
        rs2_value = self.get(rs2, unsigned=True) 

        if rs1_value >= rs2_value:
            self.cpu.pc = imm

        log_info.set_pc(imm)
        log_info.set_rs1(rs1, self.get(rs1))
        log_info.set_rs2(rs2, self.get(rs2))
        log_info.set_disassembly(f'bgey x{rs1}, x{rs2}, {imm}')

