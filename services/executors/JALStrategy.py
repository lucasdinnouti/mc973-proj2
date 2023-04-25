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
        jump_address = self.cpu.pc + imm

        self.set(rd, jump_address)
        self.cpu.pc = jump_address

        if imm < 0:
            imm += 2**32

        log_info.set_rd(rd, self.get(rd))
        log_info.set_disassembly(f'jal x{rd}, {hex(imm)}')