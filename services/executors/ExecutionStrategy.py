class ExecutionStrategy:
    def __init__(self, regs) -> None:
        self.regs = regs

    def execute(self, instr, log_info) -> int:
        pass