from modules.BUS import BUS
from utils.Logger import LogInfo
from services.Executor import Executor

import utils.Constants as const

class CPU:

    def __init__(self):
        self.regs = [0 for _ in range(32)]
        self.pc = 0
        self.bus = BUS()

    def fetch(self) -> int:
        return self.bus.load(self.pc, 32)
    
    def execute(self, instr, log_info) -> int:
        self.regs[0] = 0

        return 1
    
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

    def execute_C_TYPE(self, funct3, funct7):
        pass

    def execute_S_TYPE(self, funct3, funct7):
        pass
    
    def store_program(self, program):
        for i, instr in enumerate(program):
            self.bus.store(i * 4, 32, instr)