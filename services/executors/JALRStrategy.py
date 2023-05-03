from services.executors.ExecutionStrategy import ExecutionStrategy
from utils.Logger import LogInfo
from services.Decoder import Decoder

class JALRStrategy(ExecutionStrategy):
    def execute(self, instr, log_info: LogInfo) -> int:
        self.exec_JALR(instr, log_info)
        
    def exec_JALR(self, instr, log_info: LogInfo):
        imm = Decoder.imm_I(instr)
        rd = Decoder.rd(instr)
        rs1 = Decoder.rs1(instr)
        
        self.cpu.pc -= 4 # TODO Check if nedeed

        rs1_value = self.cpu.get(rs1)

        self.cpu.set(rd, self.cpu.pc + 4)
        self.cpu.pc = (rs1_value + imm) & ~1
        
        if imm < 0:
            imm += 2**32

        log_info.set_rd(rd, self.cpu.get(rd))
        log_info.set_disassembly(f'JALR x{rd}, {hex(imm)}')