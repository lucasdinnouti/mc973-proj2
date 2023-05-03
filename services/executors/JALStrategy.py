from services.executors.ExecutionStrategy import ExecutionStrategy
from utils.Logger import LogInfo
from services.Decoder import Decoder

class JALStrategy(ExecutionStrategy):
    def execute(self, instr, log_info: LogInfo) -> int:
        self.exec_JAL(instr, log_info)
        
    def exec_JAL(self, instr, log_info: LogInfo):
        imm = Decoder.imm_J(instr)
        rd = Decoder.rd(instr)
        
        self.cpu.pc -= 4 # TODO Check if nedeed

        self.cpu.set(rd, self.cpu.pc + 4)
        self.cpu.pc = self.cpu.pc + imm

        if imm < 0:
            imm += 2**32

        log_info.set_rd(rd, self.cpu.get(rd))
        log_info.set_disassembly(f'jal x{rd}, {hex(imm)}')