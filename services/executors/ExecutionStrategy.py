from utils.Binary import Binary as bin

class ExecutionStrategy:
    
    def __init__(self, cpu) -> None:
        self.cpu = cpu

    def execute(self, instr, log_info) -> int:
        pass
    
    # def get(self, register, unsigned=False) -> int:
    #     val = self.cpu.regs[register]

    #     return bin.twos_comp(val, 32) if unsigned else val
    
    # def set(self, register, value) -> None:
    #     self.cpu.regs[register] = value
