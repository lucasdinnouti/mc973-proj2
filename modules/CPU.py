from modules.BUS import BUS
from utils.Logger import LogInfo

import utils.Constants as const

class CPU:

    def __init__(self):
        self.regs = [0 for _ in range(32)]
        self.pc = 0
        self.bus = BUS()

    def fetch(self) -> int:
        return self.bus.load(self.pc, 32)
    
    def execute(self, instr, log_info) -> int:
        opcode = instr & 0x7f
        funct3 = (instr >> 12) & 0x7
        funct7 = (instr >> 25) & 0x7f
        
        self.regs[0] = 0

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
            self.execute_I_TYPE(instr, funct3, funct7, log_info)
        elif opcode == const.C_TYPE:
            self.execute_C_TYPE(instr, funct3, funct7, log_info)
        elif opcode == const.S_TYPE:
            self.execute_S_TYPE(instr, funct3, funct7, log_info)
        else:
            raise Exception('Cannot decode instruction type')

        return 0
    
    def execute_LUI(self, funct3, funct7):
        pass

    def execute_AUIPC(self, funct3, funct7):
        pass

    def execute_JAL(self, funct3, funct7):
        pass

    def execute_JALR(self, funct3, funct7):
        pass

    def execute_LOAD(self, funct3, funct7):
        pass

    def execute_FENCE(self, funct3, funct7):
        pass

    def execute_B_TYPE(self, funct3, funct7):
        pass

    def execute_R_TYPE(self, funct3, funct7):
        pass

    ########## I_TYPE ##########

    def execute_I_TYPE(self, instr, funct3, funct7, log_info):
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
        imm = self.imm_I(instr)
        rd = self.rd(instr)
        rs1 = self.rs1(instr)
        self.regs[rd] = self.regs[rs1] + imm

        log_info.set_rd(rd, self.regs[rd])
        log_info.set_rs1(rs1, self.regs[rs1])
        log_info.set_disassembly(f'addi	x{rd}, x{rs1}, {imm}')

    def exec_SLLI(self, instr, log_info):
        pass

    def exec_SLTI(self, instr, log_info):
        pass

    def exec_SLTIU(self, instr, log_info):
        pass

    def exec_XORI(self, instr, log_info):
        pass

    def exec_SRLI(self, instr, log_info):
        pass

    def exec_SRAI(self, instr, log_info):
        pass

    def exec_ORI(self, instr, log_info):
        pass

    def exec_ANDI(self, instr, log_info):
        pass


    ########## C_TYPE ##########

    def execute_C_TYPE(self, funct3, funct7):
        pass

    def execute_S_TYPE(self, funct3, funct7):
        pass
    
    def store_program(self, program):
        for i, instr in enumerate(program):
            self.bus.store(i, 32, instr)

#### Decoding instructions

    def rd(self, instr) -> int:
        return (instr >> 7) & 0x1f
        
    def rs1(self, instr) -> int:
        return (instr >> 15) & 0x1f 

    def rs2(self, instr) -> int:
        return (instr >> 20) & 0x1f 

    def imm_I(self, instr) -> int:
        return (instr & 0xfff00000) >> 20 

    def imm_S(self, instr) -> int:
        return ((instr & 0xfe000000) >> 20) | (instr >> 7) & 0x1f

    def imm_B(self, instr) -> int:
        return ((instr & 0x80000000) >> 19) \
            | ((instr & 0x80) << 4) \
            | ((instr >> 20) & 0x7e0) \
            | ((instr >> 7) & 0x1e)

    def imm_U(self, instr) -> int:
        return instr & 0xfffff999

    def imm_J(self, instr) -> int:
        return ((instr & 0x80000000) >> 11) \
            | (instr & 0xff000) \
            | ((instr >> 9) & 0x800) \
            | ((instr >> 20) & 0x7fe)

    def shamt(self, instr) -> int:
        return (self.imm_I(instr) & 0x1f) 
