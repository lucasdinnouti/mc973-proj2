from services.executors.ExecutionStrategy import ExecutionStrategy
from utils.Logger import LogInfo
from services.Decoder import Decoder
import utils.Constants as const

class RTypeStrategy(ExecutionStrategy):
    def execute(self, instr, log_info: LogInfo) -> int:
        funct3 = Decoder.funct3(instr)
        funct7 = Decoder.funct7(instr)

        if funct3 == const.ADD_SUB:
            if funct7 == const.AND:
                self.exec_ADD(instr, log_info)
            elif funct7 == const.SUB:
                self.exec_SUB(instr, log_info)
        elif funct3 == const.SLL:
            self.exec_SLL(instr, log_info)
        elif funct3 == const.SLT:
            self.exec_SLT(instr, log_info)
        elif funct3 == const.SLTU:
            self.exec_SLTU(instr, log_info)
        elif funct3 == const.XOR:
            self.exec_XOR(instr, log_info)
        elif funct3 == const.SR:
            if funct7 == const.SRL:
                self.exec_SRL(instr, log_info)
            elif funct7 == const.SRA:
                self.exec_SRA(instr, log_info)
        elif funct3 == const.OR:
            self.exec_OR (instr, log_info)
        elif funct3 == const.AND:
            self.exec_AND(instr, log_info)
        else:
            raise Exception('Cannot decode R_TYPE instruction')

    def exec_ADD(self, instr, log_info: LogInfo):
        rd = Decoder.rd(instr)
        rs1 = Decoder.rs1(instr)
        rs2 = Decoder.rs2(instr)
        
        self.cpu.set(rd, (self.cpu.get(rs1) + self.cpu.get(rs2)))

        log_info.set_rd(rd, self.cpu.get(rd))
        log_info.set_rs1(rs1, self.cpu.get(rs1))
        log_info.set_rs2(rs2, self.cpu.get(rs2))
        log_info.set_disassembly(f'add x{rd}, x{rs1}, x{rs2}')

    def exec_SUB(self, instr, log_info: LogInfo):
        rd = Decoder.rd(instr)
        rs1 = Decoder.rs1(instr)
        rs2 = Decoder.rs2(instr)
        
        self.cpu.set(rd, (self.cpu.get(rs1) - self.cpu.get(rs2)))

        log_info.set_rd(rd, self.cpu.get(rd))
        log_info.set_rs1(rs1, self.cpu.get(rs1))
        log_info.set_rs2(rs2, self.cpu.get(rs2))
        log_info.set_disassembly(f'sub x{rd}, x{rs1}, x{rs2}')

    def exec_SLL(self, instr, log_info: LogInfo):
        rd = Decoder.rd(instr)
        rs1 = Decoder.rs1(instr)
        rs2 = Decoder.rs2(instr)

        if self.cpu.get(rs1) >= 0:
            self.cpu.set(rd, (self.cpu.get(rs1) << rs2))
        else:
            self.cpu.set(rd, ((self.cpu.get(rs1)+0x100000000)<<rs2))

        log_info.set_rd(rd, self.cpu.get(rd))
        log_info.set_rs1(rs1, self.cpu.get(rs1))
        log_info.set_rs2(rs2, self.cpu.get(rs2))
        log_info.set_disassembly(f'sll x{rd}, x{rs1}, x{rs2}')

    def exec_SLT(self, instr, log_info: LogInfo):
        rd = Decoder.rd(instr)
        rs1 = Decoder.rs1(instr)
        rs2 = Decoder.rs2(instr)
        
        if self.cpu.get(rs1) < self.cpu.get(rs2):
            self.cpu.set(rd, (1))
        else:
            self.cpu.set(rd, (0))

        log_info.set_rd(rd, self.cpu.get(rd))
        log_info.set_rs1(rs1, self.cpu.get(rs1))
        log_info.set_rs2(rs2, self.cpu.get(rs2))
        log_info.set_disassembly(f'slt x{rd}, x{rs1}, x{rs2}')

    def exec_SLTU(self, instr, log_info: LogInfo):
        rd = Decoder.rd(instr)
        rs1 = Decoder.rs1(instr)
        rs2 = Decoder.rs2(instr)
        
        rs1_value = self.cpu.get(rs1, unsigned=True)
        rs2_value = self.cpu.get(rs2, unsigned=True)

        # TODO: check rs1 = 0
        if rs1_value < rs2_value:
            self.cpu.set(rd, (1))
        else:
            self.cpu.set(rd, (0))

        log_info.set_rd(rd, self.cpu.get(rd))
        log_info.set_rs1(rs1, self.cpu.get(rs1))
        log_info.set_rs2(rs2, self.cpu.get(rs2))
        log_info.set_disassembly(f'sltu x{rd}, x{rs1}, x{rs2}')

    def exec_XOR(self, instr, log_info: LogInfo):
        rd = Decoder.rd(instr)
        rs1 = Decoder.rs1(instr)
        rs2 = Decoder.rs2(instr)
        
        self.cpu.set(rd, (self.cpu.get(rs1) ^ self.cpu.get(rs2)))

        log_info.set_rd(rd, self.cpu.get(rd))
        log_info.set_rs1(rs1, self.cpu.get(rs1))
        log_info.set_rs2(rs2, self.cpu.get(rs2))
        log_info.set_disassembly(f'xor x{rd}, x{rs1}, x{rs2}')

    def exec_SRL(self, instr, log_info: LogInfo):
        rd = Decoder.rd(instr)
        rs1 = Decoder.rs1(instr)
        rs2 = Decoder.rs2(instr)

        if self.cpu.get(rs1) >= 0:
            self.cpu.set(rd, (self.cpu.get(rs1) >> self.cpu.get(rs2)))
        else:
            self.cpu.set(rd, ((self.cpu.get(rs1)+0x100000000)>>self.cpu.get(rs2)))

        log_info.set_rd(rd, self.cpu.get(rd))
        log_info.set_rs1(rs1, self.cpu.get(rs1))
        log_info.set_rs2(rs2, self.cpu.get(rs2))
        log_info.set_disassembly(f'srl x{rd}, x{rs1}, x{rs2}')

    def exec_SRA(self, instr, log_info: LogInfo):
        rd = Decoder.rd(instr)
        rs1 = Decoder.rs1(instr)
        rs2 = Decoder.rs2(instr)
        
        self.cpu.set(rd, (self.cpu.get(rs1) >> self.cpu.get(rs2)))

        log_info.set_rd(rd, self.cpu.get(rd))
        log_info.set_rs1(rs1, self.cpu.get(rs1))
        log_info.set_rs2(rs2, self.cpu.get(rs2))
        log_info.set_disassembly(f'sra x{rd}, x{rs1}, x{rs2}')

    def exec_OR (self, instr, log_info: LogInfo):
        rd = Decoder.rd(instr)
        rs1 = Decoder.rs1(instr)
        rs2 = Decoder.rs2(instr)
        
        self.cpu.set(rd, (self.cpu.get(rs1) | self.cpu.get(rs2)))

        log_info.set_rd(rd, self.cpu.get(rd))
        log_info.set_rs1(rs1, self.cpu.get(rs1))
        log_info.set_rs2(rs2, self.cpu.get(rs2))
        log_info.set_disassembly(f'or x{rd}, x{rs1}, x{rs2}')

    def exec_AND(self, instr, log_info: LogInfo):
        rd = Decoder.rd(instr)
        rs1 = Decoder.rs1(instr)
        rs2 = Decoder.rs2(instr)
        
        self.cpu.set(rd, (self.cpu.get(rs1) & self.cpu.get(rs2)))

        log_info.set_rd(rd, self.cpu.get(rd))
        log_info.set_rs1(rs1, self.cpu.get(rs1))
        log_info.set_rs2(rs2, self.cpu.get(rs2))
        log_info.set_disassembly(f'and x{rd}, x{rs1}, x{rs2}')