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
        for i, inst in enumerate(program):
            self.bus.store(i, 32, inst)