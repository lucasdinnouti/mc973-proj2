class ExecutionStrategy:
    def __init__(self, regs) -> None:
        self.regs = regs

    def execute(self, instr, opcode, funct3, funct7, log_info) -> int:
        pass