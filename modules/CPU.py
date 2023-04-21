from modules.BUS import BUS

class CPU:

    def __init__(self):
        self.regs = [0 for _ in range(32)]
        self.pc = 0
        self.bus = BUS()

    def fetch(self) -> int:
        return self.bus.load(self.pc, 32)
    
    def execute(self, instr) -> int:
        return 0
    
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

    def imm_B(self, instr) -> int:
        return instr & 0xfffff999

    def imm_J(self, instr) -> int:
        return ((instr & 0x80000000) >> 11) \
            | (instr & 0xff000) \
            | ((instr >> 9) & 0x800) \
            | ((instr >> 20) & 0x7fe)

    def shamt(self, instr) -> int:
        return (self.imm_I(instr) & 0x1f) 
