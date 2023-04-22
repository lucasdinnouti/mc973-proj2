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
        log_info.set_disassembly(f'addi x{rd}, x{rs1}, {imm}')

    # logical left shift
    def exec_SLLI(self, instr, log_info: LogInfo):
        shit_amount = Decoder.shamt(instr)
        rd = Decoder.rd(instr)
        rs1 = Decoder.rs1(instr)

        if self.regs[rs1] >= 0:
            self.regs[rd] = self.regs[rs1] << shit_amount
        else:
            self.regs[rd] = (self.regs[rs1]+0x100000000)<<shit_amount

        log_info.set_rd(rd, self.regs[rd])
        log_info.set_rs1(rs1, self.regs[rs1])
        log_info.set_disassembly(f'slli x{rd}, x{rs1}, {shit_amount}')

    # set less than immediate
    def exec_SLTI(self, instr, log_info: LogInfo):
        imm = Decoder.imm_I(instr)
        rd = Decoder.rd(instr)
        rs1 = Decoder.rs1(instr)
        
        if self.regs[rs1] < imm:
            self.regs[rd] = 1
        else:
            self.regs[rd] = 0

        log_info.set_rd(rd, self.regs[rd])
        log_info.set_rs1(rs1, self.regs[rs1])
        log_info.set_disassembly(f'slti x{rd}, x{rs1}, {imm}')

    # set less than immediate (unsigned)
    def exec_SLTIU(self, instr, log_info: LogInfo):
        imm = Decoder.imm_I(instr)
        rd = Decoder.rd(instr)
        rs1 = Decoder.rs1(instr)

        unsigned_rs1 = self.regs[rs1]+2**32
        unsigned_imm = imm+2**32
        
        if unsigned_rs1 < unsigned_imm:
            self.regs[rd] = 1
        else:
            self.regs[rd] = 0

        log_info.set_rd(rd, self.regs[rd])
        log_info.set_rs1(rs1, self.regs[rs1])
        log_info.set_disassembly(f'sltiu x{rd}, x{rs1}, {imm}')

    def exec_XORI(self, instr, log_info: LogInfo):
        imm = Decoder.imm_I(instr)
        rd = Decoder.rd(instr)
        rs1 = Decoder.rs1(instr)
        self.regs[rd] = self.regs[rs1] ^ imm

        log_info.set_rd(rd, self.regs[rd])
        log_info.set_rs1(rs1, self.regs[rs1])
        log_info.set_disassembly(f'xori x{rd}, x{rs1}, {imm}')

    # logical right shift
    def exec_SRLI(self, instr, log_info: LogInfo):
        shit_amount = Decoder.shamt(instr)
        rd = Decoder.rd(instr)
        rs1 = Decoder.rs1(instr)

        if self.regs[rs1] >= 0:
            self.regs[rd] = self.regs[rs1] >> shit_amount
        else:
            self.regs[rd] = (self.regs[rs1]+0x100000000)>>shit_amount

        log_info.set_rd(rd, self.regs[rd])
        log_info.set_rs1(rs1, self.regs[rs1])
        log_info.set_disassembly(f'srli x{rd}, x{rs1}, {shit_amount}')

    # arithmetic right shift
    def exec_SRAI(self, instr, log_info: LogInfo):
        shit_amount = Decoder.shamt(instr)
        rd = Decoder.rd(instr)
        rs1 = Decoder.rs1(instr)
        self.regs[rs1] = self.regs[rs1] >> shit_amount

        log_info.set_rd(rd, self.regs[rd])
        log_info.set_rs1(rs1, self.regs[rs1])
        log_info.set_disassembly(f'slli x{rd}, x{rs1}, {shit_amount}')

    def exec_ORI(self, instr, log_info: LogInfo):
        imm = Decoder.imm_I(instr)
        rd = Decoder.rd(instr)
        rs1 = Decoder.rs1(instr)
        self.regs[rd] = self.regs[rs1] | imm

        log_info.set_rd(rd, self.regs[rd])
        log_info.set_rs1(rs1, self.regs[rs1])
        log_info.set_disassembly(f'ori x{rd}, x{rs1}, {imm}')

    def exec_ANDI(self, instr, log_info: LogInfo):
        imm = Decoder.imm_I(instr)
        rd = Decoder.rd(instr)
        rs1 = Decoder.rs1(instr)
        self.regs[rd] = self.regs[rs1] & imm

        log_info.set_rd(rd, self.regs[rd])
        log_info.set_rs1(rs1, self.regs[rs1])
        log_info.set_disassembly(f'andi x{rd}, x{rs1}, {imm}')
