from utils.Binary import Binary as bin

class ExecutionStrategy:
    
    def __init__(self, cpu) -> None:
        self.cpu = cpu

    def execute(self, instr, log_info) -> int:
        pass
